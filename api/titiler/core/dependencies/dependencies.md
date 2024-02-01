# Module titiler.core.dependencies

Common dependency.

## Variables

```python3
RescaleType
```

## Functions

    
### BufferParams

```python3
def BufferParams(
    buffer: typing_extensions.Annotated[Union[float, NoneType], Query(PydanticUndefined)] = None
) -> Union[float, NoneType]
```

Tile buffer Parameter.

    
### ColorFormulaParams

```python3
def ColorFormulaParams(
    color_formula: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
) -> Union[str, NoneType]
```

ColorFormula Parameter.

    
### ColorMapParams

```python3
def ColorMapParams(
    colormap_name: typing_extensions.Annotated[Literal['deep_r', 'brbg', 'rdpu', 'hot', 'solar_r', 'gist_gray_r', 'blues_r', 'hsv', 'rplumbo', 'spring_r', 'winter', 'rdgy', 'prism_r', 'gist_stern_r', 'terrain', 'turbid', 'rain_r', 'ylorbr', 'schwarzwald', 'deep', 'ylgn_r', 'summer', 'bupu', 'gist_ncar', 'set1', 'tab20c', 'delta', 'delta_r', 'tarn_r', 'dark2_r', 'thermal', 'oxy', 'set2_r', 'jet', 'rainbow_r', 'plasma', 'dense', 'tab20c_r', 'oranges', 'phase', 'accent', 'magma', 'autumn', 'diff', 'speed', 'pink_r', 'ylorrd_r', 'set2', 'rainbow', 'curl_r', 'orrd_r', 'pubu', 'prgn', 'pastel1_r', 'matter', 'puor', 'gist_earth_r', 'gist_heat_r', 'set3', 'cfastie', 'haline_r', 'rdylgn_r', 'purd', 'gnuplot2', 'greens', 'ylgnbu_r', 'inferno', 'tab20b', 'inferno_r', 'twilight_shifted_r', 'piyg', 'summer_r', 'purd_r', 'bwr_r', 'seismic', 'phase_r', 'coolwarm_r', 'ice_r', 'thermal_r', 'curl', 'algae_r', 'brg_r', 'gnuplot2_r', 'gist_yarg', 'pubu_r', 'winter_r', 'gray_r', 'speed_r', 'wistia_r', 'topo', 'gist_gray', 'cubehelix', 'blues', 'terrain_r', 'brbg_r', 'balance', 'oranges_r', 'matter_r', 'bugn', 'gist_rainbow', 'diff_r', 'amp_r', 'spectral', 'pink', 'cubehelix_r', 'ocean', 'jet_r', 'set1_r', 'ocean_r', 'binary', 'puor_r', 'twilight_r', 'algae', 'hsv_r', 'magma_r', 'purples', 'prism', 'rain', 'pastel1', 'spring', 'nipy_spectral_r', 'accent_r', 'rdbu', 'set3_r', 'twilight', 'plasma_r', 'orrd', 'paired', 'pastel2_r', 'greys', 'viridis', 'cool_r', 'turbo', 'pastel2', 'cmrmap', 'piyg_r', 'amp', 'gnuplot', 'turbo_r', 'pubugn', 'rdylbu_r', 'paired_r', 'cmrmap_r', 'brg', 'tarn', 'reds_r', 'viridis_r', 'gnbu_r', 'bugn_r', 'afmhot_r', 'flag_r', 'greens_r', 'ice', 'copper_r', 'tab20b_r', 'wistia', 'bupu_r', 'rdgy_r', 'tempo', 'copper', 'tab20_r', 'binary_r', 'ylgn', 'rdylbu', 'autumn_r', 'ylorrd', 'nipy_spectral', 'gist_ncar_r', 'rdylgn', 'rdbu_r', 'cividis', 'tempo_r', 'seismic_r', 'purples_r', 'pubugn_r', 'cool', 'haline', 'dark2', 'topo_r', 'balance_r', 'greys_r', 'spectral_r', 'ylgnbu', 'gnuplot_r', 'gist_earth', 'gnbu', 'dense_r', 'tab10_r', 'twilight_shifted', 'gist_rainbow_r', 'turbid_r', 'tab20', 'ylorbr_r', 'tab10', 'cividis_r', 'gist_yarg_r', 'oxy_r', 'prgn_r', 'gray', 'rdpu_r', 'reds', 'bone_r', 'solar', 'hot_r', 'gist_heat', 'flag', 'afmhot', 'bwr', 'coolwarm', 'bone', 'gist_stern'], Query(PydanticUndefined)] = None,
    colormap: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
)
```

    
### CoordCRSParams

```python3
def CoordCRSParams(
    crs: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
) -> Union[rasterio.crs.CRS, NoneType]
```

Coordinate Reference System Coordinates Param.

    
### DatasetPathParams

```python3
def DatasetPathParams(
    url: typing_extensions.Annotated[str, Query(PydanticUndefined)]
) -> str
```

Create dataset path from args

    
### DstCRSParams

```python3
def DstCRSParams(
    crs: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
) -> Union[rasterio.crs.CRS, NoneType]
```

Coordinate Reference System Coordinates Param.

    
### RescalingParams

```python3
def RescalingParams(
    rescale: typing_extensions.Annotated[Union[List[str], NoneType], Query(PydanticUndefined)] = None
) -> Union[List[Tuple[float, ...]], NoneType]
```

Min/Max data Rescaling

    
### create_colormap_dependency

```python3
def create_colormap_dependency(
    cmap: rio_tiler.colormap.ColorMaps
) -> Callable
```

Create Colormap Dependency.

## Classes

### AssetsBidxExprParams

```python3
class AssetsBidxExprParams(
    indexes: typing_extensions.Annotated[Union[List[int], NoneType], Query(PydanticUndefined)] = None,
    assets: typing_extensions.Annotated[Union[List[str], NoneType], Query(PydanticUndefined)] = None,
    expression: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None,
    asset_indexes: typing_extensions.Annotated[Union[Sequence[str], NoneType], Query(PydanticUndefined)] = None,
    asset_as_band: typing_extensions.Annotated[Union[bool, NoneType], Query(PydanticUndefined)] = None
)
```

Assets, Expression and Asset's band Indexes parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.AssetsParams
* titiler.core.dependencies.BidxParams
* titiler.core.dependencies.DefaultDependency

#### Descendants

* titiler.core.dependencies.AssetsBidxExprParamsOptional

#### Class variables

```python3
asset_as_band
```

```python3
asset_indexes
```

```python3
assets
```

```python3
expression
```

```python3
indexes
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### AssetsBidxExprParamsOptional

```python3
class AssetsBidxExprParamsOptional(
    indexes: typing_extensions.Annotated[Union[List[int], NoneType], Query(PydanticUndefined)] = None,
    assets: typing_extensions.Annotated[Union[List[str], NoneType], Query(PydanticUndefined)] = None,
    expression: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None,
    asset_indexes: typing_extensions.Annotated[Union[Sequence[str], NoneType], Query(PydanticUndefined)] = None,
    asset_as_band: typing_extensions.Annotated[Union[bool, NoneType], Query(PydanticUndefined)] = None
)
```

Assets, Expression and Asset's band Indexes parameters but with no requirement.

#### Ancestors (in MRO)

* titiler.core.dependencies.AssetsBidxExprParams
* titiler.core.dependencies.AssetsParams
* titiler.core.dependencies.BidxParams
* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
asset_as_band
```

```python3
asset_indexes
```

```python3
assets
```

```python3
expression
```

```python3
indexes
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### AssetsBidxParams

```python3
class AssetsBidxParams(
    indexes: typing_extensions.Annotated[Union[List[int], NoneType], Query(PydanticUndefined)] = None,
    assets: typing_extensions.Annotated[Union[List[str], NoneType], Query(PydanticUndefined)] = None,
    asset_indexes: typing_extensions.Annotated[Union[Sequence[str], NoneType], Query(PydanticUndefined)] = None,
    asset_expression: typing_extensions.Annotated[Union[Sequence[str], NoneType], Query(PydanticUndefined)] = None
)
```

Assets, Asset's band Indexes and Asset's band Expression parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.AssetsParams
* titiler.core.dependencies.BidxParams
* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
asset_expression
```

```python3
asset_indexes
```

```python3
assets
```

```python3
indexes
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### AssetsParams

```python3
class AssetsParams(
    assets: typing_extensions.Annotated[Union[List[str], NoneType], Query(PydanticUndefined)] = None
)
```

Assets parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Descendants

* titiler.core.dependencies.AssetsBidxExprParams
* titiler.core.dependencies.AssetsBidxParams

#### Class variables

```python3
assets
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### BandsExprParams

```python3
class BandsExprParams(
    bands: typing_extensions.Annotated[Union[List[str], NoneType], Query(PydanticUndefined)] = None,
    expression: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
)
```

Band names and Expression parameters (Band or Expression required).

#### Ancestors (in MRO)

* titiler.core.dependencies.ExpressionParams
* titiler.core.dependencies.BandsParams
* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
bands
```

```python3
expression
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### BandsExprParamsOptional

```python3
class BandsExprParamsOptional(
    bands: typing_extensions.Annotated[Union[List[str], NoneType], Query(PydanticUndefined)] = None,
    expression: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
)
```

Optional Band names and Expression parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.ExpressionParams
* titiler.core.dependencies.BandsParams
* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
bands
```

```python3
expression
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### BandsParams

```python3
class BandsParams(
    bands: typing_extensions.Annotated[Union[List[str], NoneType], Query(PydanticUndefined)] = None
)
```

Band names parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Descendants

* titiler.core.dependencies.BandsExprParamsOptional
* titiler.core.dependencies.BandsExprParams

#### Class variables

```python3
bands
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### BidxExprParams

```python3
class BidxExprParams(
    indexes: typing_extensions.Annotated[Union[List[int], NoneType], Query(PydanticUndefined)] = None,
    expression: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
)
```

Band Indexes and Expression parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.ExpressionParams
* titiler.core.dependencies.BidxParams
* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
expression
```

```python3
indexes
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### BidxParams

```python3
class BidxParams(
    indexes: typing_extensions.Annotated[Union[List[int], NoneType], Query(PydanticUndefined)] = None
)
```

Band Indexes parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Descendants

* titiler.core.dependencies.BidxExprParams
* titiler.core.dependencies.AssetsBidxExprParams
* titiler.core.dependencies.AssetsBidxParams

#### Class variables

```python3
indexes
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### DatasetParams

```python3
class DatasetParams(
    nodata: typing_extensions.Annotated[Union[str, int, float, NoneType], Query(PydanticUndefined)] = None,
    unscale: typing_extensions.Annotated[bool, Query(PydanticUndefined)] = False,
    resampling_method: typing_extensions.Annotated[Literal['nearest', 'bilinear', 'cubic', 'cubic_spline', 'lanczos', 'average', 'mode', 'gauss', 'rms'], Query(PydanticUndefined)] = 'nearest',
    reproject_method: typing_extensions.Annotated[Literal['nearest', 'bilinear', 'cubic', 'cubic_spline', 'lanczos', 'average', 'mode', 'sum', 'rms'], Query(PydanticUndefined)] = 'nearest'
)
```

Low level WarpedVRT Optional parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
nodata
```

```python3
reproject_method
```

```python3
resampling_method
```

```python3
unscale
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### DefaultDependency

```python3
class DefaultDependency(
    
)
```

Dataclass with dict unpacking

#### Descendants

* titiler.core.dependencies.BidxParams
* titiler.core.dependencies.ExpressionParams
* titiler.core.dependencies.AssetsParams
* titiler.core.dependencies.BandsParams
* titiler.core.dependencies.PreviewParams
* titiler.core.dependencies.PartFeatureParams
* titiler.core.dependencies.DatasetParams
* titiler.core.dependencies.ImageRenderingParams
* titiler.core.dependencies.StatisticsParams
* titiler.core.dependencies.HistogramParams
* titiler.core.dependencies.TileParams

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### ExpressionParams

```python3
class ExpressionParams(
    expression: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
)
```

Expression parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Descendants

* titiler.core.dependencies.BidxExprParams
* titiler.core.dependencies.BandsExprParamsOptional
* titiler.core.dependencies.BandsExprParams

#### Class variables

```python3
expression
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### HistogramParams

```python3
class HistogramParams(
    bins: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None,
    range: typing_extensions.Annotated[Union[str, NoneType], Query(PydanticUndefined)] = None
)
```

Numpy Histogram options.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
bins
```

```python3
range
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### ImageRenderingParams

```python3
class ImageRenderingParams(
    add_mask: typing_extensions.Annotated[bool, Query(PydanticUndefined)] = True
)
```

Image Rendering options.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
add_mask
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### PartFeatureParams

```python3
class PartFeatureParams(
    max_size: typing_extensions.Annotated[Union[int, NoneType], 'Maximum image size to read onto.'] = None,
    height: typing_extensions.Annotated[Union[int, NoneType], 'Force output image height.'] = None,
    width: typing_extensions.Annotated[Union[int, NoneType], 'Force output image width.'] = None
)
```

Common parameters for bbox and feature.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
height
```

```python3
max_size
```

```python3
width
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### PreviewParams

```python3
class PreviewParams(
    max_size: typing_extensions.Annotated[int, 'Maximum image size to read onto.'] = 1024,
    height: typing_extensions.Annotated[Union[int, NoneType], 'Force output image height.'] = None,
    width: typing_extensions.Annotated[Union[int, NoneType], 'Force output image width.'] = None
)
```

Common Preview parameters.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
height
```

```python3
max_size
```

```python3
width
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### StatisticsParams

```python3
class StatisticsParams(
    categorical: typing_extensions.Annotated[bool, Query(PydanticUndefined)] = False,
    categories: typing_extensions.Annotated[Union[List[Union[float, int]], NoneType], Query(PydanticUndefined)] = None,
    percentiles: typing_extensions.Annotated[Union[List[int], NoneType], Query(PydanticUndefined)] = None
)
```

Statistics options.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
categorical
```

```python3
categories
```

```python3
percentiles
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.

### TileParams

```python3
class TileParams(
    buffer: typing_extensions.Annotated[Union[float, NoneType], Query(PydanticUndefined)] = None,
    padding: typing_extensions.Annotated[Union[int, NoneType], Query(PydanticUndefined)] = None
)
```

Tile options.

#### Ancestors (in MRO)

* titiler.core.dependencies.DefaultDependency

#### Class variables

```python3
buffer
```

```python3
padding
```

#### Methods

    
#### keys

```python3
def keys(
    self
)
```

Return Keys.