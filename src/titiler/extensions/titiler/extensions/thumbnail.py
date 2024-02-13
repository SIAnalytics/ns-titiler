from dataclasses import dataclass, field
from typing import Tuple, List, Optional

import rasterio
from starlette.responses import Response
from fastapi import Depends, FastAPI, Query
from titiler.core.factory import BaseTilerFactory, FactoryExtension, TilerFactory
from titiler.core.dependencies import RescalingParams
from titiler.core.factory import TilerFactory
from titiler.core.resources.enums import ImageType

@dataclass
class thumbnailExtension(FactoryExtension):
    """Add endpoint to a TilerFactory."""

    # Set some options
    max_size: int = field(default=128)

    # Register method is mandatory and must take a BaseTilerFactory object as input
    def register(self, factory: BaseTilerFactory):
        """Register endpoint to the tiler factory."""

        # register an endpoint to the factory's router
        @factory.router.get(
            "/thumbnail",
            responses={
                200: {
                    "content": {
                        "image/png": {},
                        "image/jpeg": {},
                    },
                    "description": "Return an image.",
                }
            },
            response_class=Response,
        )
        def thumbnail(
            # we can reuse the factory dependency
            src_path: str = Depends(factory.path_dependency),
            layer_params=Depends(factory.layer_dependency),
            dataset_params=Depends(factory.dataset_dependency),
            post_process=Depends(factory.process_dependency),
            rescale: Optional[List[Tuple[float, ...]]] = Depends(RescalingParams),
            color_formula: Optional[str] = Query(
                None,
                title="Color Formula",
                description="rio-color formula (info: https://github.com/mapbox/rio-color)",
            ),
            colormap=Depends(factory.colormap_dependency),
            render_params=Depends(factory.render_dependency),
            reader_params=Depends(factory.reader_dependency),
            env=Depends(factory.environment_dependency),
        ):
            with rasterio.Env(**env):
                with factory.reader(src_path, **reader_params) as src:
                    image = src.preview(
                        max_size=self.max_size,
                        **layer_params,
                        **dataset_params,
                    )

            if post_process:
                image = post_process(image)

            if rescale:
                image.rescale(rescale)

            if color_formula:
                image.apply_color_formula(color_formula)

            format = ImageType.jpeg if image.mask.all() else ImageType.png

            content = image.render(
                img_format=format.driver,
                colormap=colormap,
                **format.profile,
                **render_params,
            )

            return Response(content, media_type=format.mediatype)