# Module titiler.mosaic.factory

TiTiler.mosaic Router factories.

## Variables

```python3
MAX_THREADS
```

```python3
WGS84_CRS
```

```python3
img_endpoint_params
```

## Functions

    
### PixelSelectionParams

```python3
def PixelSelectionParams(
    pixel_selection: typing_extensions.Annotated[Literal['first', 'highest', 'lowest', 'mean', 'median', 'stdev', 'lastbandlow', 'lastbandhight'], Query(PydanticUndefined)] = 'first'
) -> rio_tiler.mosaic.methods.base.MosaicMethodBase
```

Returns the mosaic method used to combine datasets together.

## Classes

### MosaicTilerFactory

```python3
class MosaicTilerFactory(
    reader: Type[cogeo_mosaic.backends.base.BaseBackend] = <function MosaicBackend at 0x7f3aa25dc9d0>,
    router: fastapi.routing.APIRouter = <factory>,
    path_dependency: Callable[..., Any] = <function DatasetPathParams at 0x7f3aa1961ca0>,
    layer_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.BidxExprParams'>,
    dataset_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.DatasetParams'>,
    process_dependency: Callable[..., Union[titiler.core.algorithm.base.BaseAlgorithm, NoneType]] = <function Algorithms.dependency.<locals>.post_process at 0x7f3aa1690dc0>,
    rescale_dependency: Callable[..., Union[List[Tuple[float, ...]], NoneType]] = <function RescalingParams at 0x7f3aa1961d30>,
    color_formula_dependency: Callable[..., Union[str, NoneType]] = <function ColorFormulaParams at 0x7f3aa1873e50>,
    colormap_dependency: Callable[..., Union[Dict[int, Tuple[int, int, int, int]], Sequence[Tuple[Tuple[Union[float, int], Union[float, int]], Tuple[int, int, int, int]]], NoneType]] = <function create_colormap_dependency.<locals>.deps at 0x7f3aa1961c10>,
    render_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.ImageRenderingParams'>,
    reader_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.DefaultDependency'>,
    environment_dependency: Callable[..., Dict] = <function BaseTilerFactory.<lambda> at 0x7f3aa1755dc0>,
    supported_tms: morecantile.defaults.TileMatrixSets = TileMatrixSets(tms={'CDB1GlobalGrid': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/CDB1GlobalGrid.json'), 'CanadianNAD83_LCC': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/CanadianNAD83_LCC.json'), 'EuropeanETRS89_LAEAQuad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/EuropeanETRS89_LAEAQuad.json'), 'GNOSISGlobalGrid': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/GNOSISGlobalGrid.json'), 'LINZAntarticaMapTilegrid': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/LINZAntarticaMapTilegrid.json'), 'NZTM2000Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/NZTM2000Quad.json'), 'UPSAntarcticWGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/UPSAntarcticWGS84Quad.json'), 'UPSArcticWGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/UPSArcticWGS84Quad.json'), 'UTM31WGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/UTM31WGS84Quad.json'), 'WGS1984Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/WGS1984Quad.json'), 'WebMercatorQuad': <TileMatrixSet title='Google Maps Compatible for the World' id='WebMercatorQuad' crs='http://www.opengis.net/def/crs/EPSG/0/3857>, 'WorldCRS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/WorldCRS84Quad.json'), 'WorldMercatorWGS84Quad': PosixPath('/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/morecantile/data/WorldMercatorWGS84Quad.json')}),
    default_tms: str = 'WebMercatorQuad',
    router_prefix: str = '',
    optional_headers: List[titiler.core.resources.enums.OptionalHeader] = <factory>,
    route_dependencies: List[Tuple[List[titiler.core.routing.EndpointScope], List[fastapi.params.Depends]]] = <factory>,
    extensions: List[titiler.core.factory.FactoryExtension] = <factory>,
    templates: starlette.templating.Jinja2Templates = <starlette.templating.Jinja2Templates object at 0x7f3aa1692af0>,
    dataset_reader: Union[Type[rio_tiler.io.base.BaseReader], Type[rio_tiler.io.base.MultiBaseReader], Type[rio_tiler.io.base.MultiBandReader]] = <class 'rio_tiler.io.rasterio.Reader'>,
    backend_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.DefaultDependency'>,
    pixel_selection_dependency: Callable[..., rio_tiler.mosaic.methods.base.MosaicMethodBase] = <function PixelSelectionParams at 0x7f3aa25dc8b0>,
    tile_dependency: Type[titiler.core.dependencies.DefaultDependency] = <class 'titiler.core.dependencies.TileParams'>,
    add_viewer: bool = True
)
```

MosaicTiler Factory.

The main difference with titiler.endpoint.factory.TilerFactory is that this factory
needs the `reader` to be of `cogeo_mosaic.backends.BaseBackend` type (e.g MosaicBackend) and a `dataset_reader` (BaseReader).

#### Ancestors (in MRO)

* titiler.core.factory.BaseTilerFactory

#### Class variables

```python3
add_viewer
```

```python3
backend_dependency
```

```python3
dataset_dependency
```

```python3
dataset_reader
```

```python3
default_tms
```

```python3
layer_dependency
```

```python3
reader_dependency
```

```python3
render_dependency
```

```python3
router_prefix
```

```python3
supported_tms
```

```python3
templates
```

```python3
tile_dependency
```

#### Methods

    
#### add_route_dependencies

```python3
def add_route_dependencies(
    self,
    *,
    scopes: List[titiler.core.routing.EndpointScope],
    dependencies=typing.List[fastapi.params.Depends]
)
```

Add dependencies to routes.

Allows a developer to add dependencies to a route after the route has been defined.

    
#### assets

```python3
def assets(
    self
)
```

Register /assets endpoint.

    
#### bounds

```python3
def bounds(
    self
)
```

Register /bounds endpoint.

    
#### color_formula_dependency

```python3
def color_formula_dependency(
    color_formula: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
) -> Union[str, NoneType]
```

ColorFormula Parameter.

    
#### colormap_dependency

```python3
def colormap_dependency(
    colormap_name: typing_extensions.Annotated[Literal['deep_r', 'brbg', 'rdpu', 'hot', 'solar_r', 'gist_gray_r', 'blues_r', 'hsv', 'rplumbo', 'spring_r', 'winter', 'rdgy', 'prism_r', 'gist_stern_r', 'terrain', 'turbid', 'rain_r', 'ylorbr', 'schwarzwald', 'deep', 'ylgn_r', 'summer', 'bupu', 'gist_ncar', 'set1', 'tab20c', 'delta', 'delta_r', 'tarn_r', 'dark2_r', 'thermal', 'oxy', 'set2_r', 'jet', 'rainbow_r', 'plasma', 'dense', 'tab20c_r', 'oranges', 'phase', 'accent', 'magma', 'autumn', 'diff', 'speed', 'pink_r', 'ylorrd_r', 'set2', 'rainbow', 'curl_r', 'orrd_r', 'pubu', 'prgn', 'pastel1_r', 'matter', 'puor', 'gist_earth_r', 'gist_heat_r', 'set3', 'cfastie', 'haline_r', 'rdylgn_r', 'purd', 'gnuplot2', 'greens', 'ylgnbu_r', 'inferno', 'tab20b', 'inferno_r', 'twilight_shifted_r', 'piyg', 'summer_r', 'purd_r', 'bwr_r', 'seismic', 'phase_r', 'coolwarm_r', 'ice_r', 'thermal_r', 'curl', 'algae_r', 'brg_r', 'gnuplot2_r', 'gist_yarg', 'pubu_r', 'winter_r', 'gray_r', 'speed_r', 'wistia_r', 'topo', 'gist_gray', 'cubehelix', 'blues', 'terrain_r', 'brbg_r', 'balance', 'oranges_r', 'matter_r', 'bugn', 'gist_rainbow', 'diff_r', 'amp_r', 'spectral', 'pink', 'cubehelix_r', 'ocean', 'jet_r', 'set1_r', 'ocean_r', 'binary', 'puor_r', 'twilight_r', 'algae', 'hsv_r', 'magma_r', 'purples', 'prism', 'rain', 'pastel1', 'spring', 'nipy_spectral_r', 'accent_r', 'rdbu', 'set3_r', 'twilight', 'plasma_r', 'orrd', 'paired', 'pastel2_r', 'greys', 'viridis', 'cool_r', 'turbo', 'pastel2', 'cmrmap', 'piyg_r', 'amp', 'gnuplot', 'turbo_r', 'pubugn', 'rdylbu_r', 'paired_r', 'cmrmap_r', 'brg', 'tarn', 'reds_r', 'viridis_r', 'gnbu_r', 'bugn_r', 'afmhot_r', 'flag_r', 'greens_r', 'ice', 'copper_r', 'tab20b_r', 'wistia', 'bupu_r', 'rdgy_r', 'tempo', 'copper', 'tab20_r', 'binary_r', 'ylgn', 'rdylbu', 'autumn_r', 'ylorrd', 'nipy_spectral', 'gist_ncar_r', 'rdylgn', 'rdbu_r', 'cividis', 'tempo_r', 'seismic_r', 'purples_r', 'pubugn_r', 'cool', 'haline', 'dark2', 'topo_r', 'balance_r', 'greys_r', 'spectral_r', 'ylgnbu', 'gnuplot_r', 'gist_earth', 'gnbu', 'dense_r', 'tab10_r', 'twilight_shifted', 'gist_rainbow_r', 'turbid_r', 'tab20', 'ylorbr_r', 'tab10', 'cividis_r', 'gist_yarg_r', 'oxy_r', 'prgn_r', 'gray', 'rdpu_r', 'reds', 'bone_r', 'solar', 'hot_r', 'gist_heat', 'flag', 'afmhot', 'bwr', 'coolwarm', 'bone', 'gist_stern'], Query(PydanticUndefined)] = None,
    colormap: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
)
```

    
#### environment_dependency

```python3
def environment_dependency(
    
)
```

    
#### info

```python3
def info(
    self
)
```

Register /info endpoint

    
#### map_viewer

```python3
def map_viewer(
    self
)
```

Register /map endpoint.

    
#### path_dependency

```python3
def path_dependency(
    url: typing_extensions.Annotated[str, Query(PydanticUndefined)]
) -> str
```

Create dataset path from args

    
#### pixel_selection_dependency

```python3
def pixel_selection_dependency(
    pixel_selection: typing_extensions.Annotated[Literal['first', 'highest', 'lowest', 'mean', 'median', 'stdev', 'lastbandlow', 'lastbandhight'], Query(PydanticUndefined)] = 'first'
) -> rio_tiler.mosaic.methods.base.MosaicMethodBase
```

Returns the mosaic method used to combine datasets together.

    
#### point

```python3
def point(
    self
)
```

Register /point endpoint.

    
#### process_dependency

```python3
def process_dependency(
    algorithm: typing_extensions.Annotated[Literal['hillshade', 'contours', 'normalizedIndex', 'terrarium', 'terrainrgb'], Query(PydanticUndefined)] = None,
    algorithm_params: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
) -> Union[titiler.core.algorithm.base.BaseAlgorithm, NoneType]
```

Data Post-Processing options.

    
#### read

```python3
def read(
    self
)
```

Register / (Get) Read endpoint.

    
#### reader

```python3
def reader(
    input: str,
    *args: Any,
    **kwargs: Any
) -> cogeo_mosaic.backends.base.BaseBackend
```

Select mosaic backend for input.

    
#### register_routes

```python3
def register_routes(
    self
)
```

This Method register routes to the router.

Because we wrap the endpoints in a class we cannot define the routes as
methods (because of the self argument). The HACK is to define routes inside
the class method and register them after the class initialization.

    
#### rescale_dependency

```python3
def rescale_dependency(
    rescale: typing_extensions.Annotated[Union[List[str], NoneType], Query(PydanticUndefined)] = None
) -> Union[List[Tuple[float, ...]], NoneType]
```

Min/Max data Rescaling

    
#### tile

```python3
def tile(
    self
)
```

Register /tiles endpoints.

    
#### tilejson

```python3
def tilejson(
    self
)
```

Add tilejson endpoint.

    
#### url_for

```python3
def url_for(
    self,
    request: starlette.requests.Request,
    name: str,
    **path_params: Any
) -> str
```

Return full url (with prefix) for a specific endpoint.

    
#### validate

```python3
def validate(
    self
)
```

Register /validate endpoint.

    
#### wmts

```python3
def wmts(
    self
)
```

Add wmts endpoint.