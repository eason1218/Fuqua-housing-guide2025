import folium
import json
import shapely.geometry
import geopandas as gpd
from folium import IFrame
from folium.plugins import FloatImage
from folium import DivIcon
# 文件路径
boundary_geojson_path = "City_of_Durham_Boundary.geojson"
road_geojson_path = "Roads.geojson"

# 读取 City of Durham 边界数据
with open(boundary_geojson_path, "r", encoding="utf-8") as f:
    boundary_data = json.load(f)

# 读取道路网络数据并处理 MultiLineString 几何
with open(road_geojson_path, "r", encoding="utf-8") as f:
    road_data = json.load(f)

road_features = []
for feature in road_data["features"]:
    geom = shapely.geometry.shape(feature["geometry"])
    if isinstance(geom, shapely.geometry.MultiLineString):
        for line in geom.geoms:
            road_features.append({"geometry": line, **feature["properties"]})
    else:
        road_features.append({"geometry": geom, **feature["properties"]})

# 创建道路的 GeoDataFrame
road_gdf = gpd.GeoDataFrame(road_features, crs="EPSG:4326")

# 创建 Folium 地图对象，并启用比例尺
m = folium.Map(location=[36.001465, -78.939133], zoom_start=13, control_scale=True)

# 创建自定义指北针 HTML
compass_html = """
<div id="compass" style="
    position: fixed;
    top: 35px; left: 50px;
    font-size: 24px;
    font-weight: bold;
    color: black;
    background-color: white;
    padding: 8px 6px;
    border-radius: 5px;
    border: 2px solid black;
    z-index: 9999;
    text-align: center;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.5);
"><div style="font-size: 8px; font-weight: bold;">N</div>
    <div style="font-size: 15px;">↑</div>
</div>
"""


# 1️⃣ 添加 **自定义 Leaflet Pane**（确保指北针可见）
m.get_root().html.add_child(folium.Element("""
    <style>
        .leaflet-top.leaflet-left { 
            z-index: 9999 !important; 
        }
    </style>
"""))


# 3️⃣ **尝试直接插入 HTML**
m.get_root().html.add_child(folium.Element(compass_html))

# 绘制 City of Durham 边界
for feature in boundary_data["features"]:
    geom = shapely.geometry.shape(feature["geometry"])
    if isinstance(geom, shapely.geometry.MultiPolygon):
        for polygon in geom.geoms:
            folium.Polygon(
                locations=[(pt[1], pt[0]) for pt in polygon.exterior.coords],
                color='black',
                weight=1
            ).add_to(m)
    elif isinstance(geom, shapely.geometry.Polygon):
        folium.Polygon(
            locations=[(pt[1], pt[0]) for pt in geom.exterior.coords],
            color='black',
            weight=1
        ).add_to(m)

# 绘制道路网络
for _, row in road_gdf.iterrows():
    geom = row['geometry']
    if isinstance(geom, shapely.geometry.LineString):
        folium.PolyLine(
            locations=[(pt[1], pt[0]) for pt in geom.coords],
            color='gray',
            weight=0.5
        ).add_to(m)
    elif isinstance(geom, shapely.geometry.MultiLineString):
        for line in geom.geoms:
            folium.PolyLine(
                locations=[(pt[1], pt[0]) for pt in line.coords],
                color='gray',
                weight=0.5
            ).add_to(m)

# 添加杜克大学的位置，使用红色星号标记
folium.Marker(
    location=[36.00142, -78.939824],
    popup='Duke University',
    icon=folium.Icon(color='red', icon='star')
).add_to(m)

folium.Marker(
    location=[35.99853, -78.94591],
    popup='Fuqua School of Business',
    icon=folium.Icon(color='green', icon='star')
).add_to(m)

# 物业列表：名称、评分、价格级别、纬度、经度
# 物业列表（包含 33 个物业）
properties = [
    ("501 Estates", 7.6, "$", 35.96624, -78.97838, "https://j501estates.com/?utm_source=apartmentseo&utm_medium=gmb&utm_campaign=organicmaplisting"),
    ("810 Ninth Street", 7.9, "$$", 36.01125, -78.92147, "https://www.810ninth.com/?ilm=onlinebusinesslisting&utm_source=obl&utm_medium=organic"),
    ("Avalon Durham", 7.5, "$$$$", 36.00966, -78.92735, "https://www.avaloncommunities.com/north-carolina/durham-apartments/avalon-durham/?utm_source=gmb&utm_medium=organic&utm_campaign=gmblist"),
    ("Beckon", 9.0, "$$$", 36.00092, -78.90472, "https://www.livebeckon.com/?switch_cls[id]=64893&utm_source=obl&utm_medium=organic"),
    ("Berkshire Main Street", 8.1, "$$$$", 36.00873, -78.92871, "https://www.berkshiremainstreet.com/"),
    ("Berkshire Ninth Street", 8.1, "$$$", 36.00849, -78.92431, "https://www.berkshireninthstreet.com/"),
    ("Blue Leaf Apartments", 9.4, "$$", 36.00847, -78.95321, "http://www.liveatblueleaf.com/"),
    ("Camden Durham", 7.9, "$$", 35.99018, -78.89978, "https://www.camdenliving.com/apartments/durham-nc/camden-durham?utm_source=gmb&utm_medium=local&utm_campaign=camden-durham&y_source=1_MjkzMTE0NjQtNzE1LWxvY2F0aW9uLndlYnNpdGU%3D"),
    ("Chapel Tower Apartments", 6.8, "$$", 36.00426, -78.95235, "https://gscapts.com/apartments/north-carolina/chapel-tower?y_source=1_MTUyOTEyODItNzE1LWxvY2F0aW9uLndlYnNpdGU%3D"),
    ("Cortland Bull City", 8.3, "$$$", 35.99409, -78.90847, "https://cortland.com/apartments/cortland-bull-city/?utm_source=gmb_site&utm_medium=organic"),
    ("Crowne at 501", 9.3, "$$$$", 35.95154, -78.99142, "http://www.crowneat501.com/"),
    ("Duke Manor", 7.4, "$", 36.01247, -78.94611, "https://gscapts.com/apartments/north-carolina/duke-manor?y_source=1_MTUyOTEyODYtNzE1LWxvY2F0aW9uLndlYnNpdGU%3D"),
    ("Foster on the Park", 9.0, "$$$$", 36.00183, -78.90177, "https://fosteronthepark.com/"),
    ("Garrett West", 8.5, "$", 35.96436, -78.97763, "https://www.garrettwestapts.com/?ilm=obl&utm_source=obl&utm_medium=organic"),
    ("Lancaster Commons", 8.2, "$$$", 35.97822, -78.95789, "https://lancastercommonsnorth.ticonproperties.com/"),
    ("Lancaster Commons North", 10.0, "$$$", 35.98055, -78.95652, "https://lancastercommonsnorth.ticonproperties.com/"),
    ("Liberty Warehouse", 8.9, "$$", 36.00117, -78.90131, "https://www.livelibertywarehouse.com/?utm_source=obl&utm_medium=organic"),
    ("Lofts at Lakeview", 7.3, "$$$", 36.00910, -78.94627, "https://loftsatlakeview.com/schedule-tour/"),
    ("One City Center", 8.9, "$$$$", 35.99579, -78.90161, "https://www.apartmentsatonecitycenter.com/?utm_source=gbp&utm_medium=organic&utm_knock=g"),
    ("Poplar West", 7.5, "$", 36.00852, -78.94919, "http://www.trinitypropertiesapartments.com/poplar-west.html"),
    ("Station Nine", 7.3, "$$$", 36.00938, -78.92523, "https://www.stationnine.com/?utm_source=GoogleMyBusiness&utm_medium=organic&utm_campaign=GMB"),
    ("Terrazzo Durham", 9.5, "$$$$", 36.00606, -78.94833, "https://terrazzodurham.com/?utm_source=google+local&utm_medium=organic&utm_campaign=website+link"),
    ("The Bailey Apartments", 6.6, "$", 35.95387, -78.96785, "https://www.thebaileyapartments.com/the-bailey-apartments-durham-nc/"),
    ("The Belmont Apartments", 8.0, "$", 36.01125, -78.94828, "https://www.livebelmont.com/?utm_knock=g"),
    ("The Heights at LaSalle", 7.8, "$$", 36.01200, -78.94936, "http://www.heightslasalle.com/?rcstdid=Mg%3D%3D-YRjTEizZPgM%3D"),
    ("The Ramsey", 9.3, "$$$$", 35.98919, -78.89768, "https://www.theramseydurham.com/?utm_source=google+local&utm_medium=organic&utm_campaign=website+link"),
    ("The Residences at Erwin Mill", 7.8, "$$$", 36.00805, -78.92323, "https://trinitycommons.com/?utm_source=googlebusiness&utm_medium=organic&utm_campaign=googlebusiness"),
    ("Trinity Commons at Erwin", 9.0, "$$$", 36.00898, -78.94405, "https://trinitycommons.com/schedule-a-tour/"),
    ("UHill Apartments", 8.2, "$$", 35.96742, -78.95260, "https://www.universityhilldurham.com/university-hill-apartments-durham-nc/"),
    ("Van Alen Apartments", 7.0, "$$$", 35.99137, -78.902250, "https://livevanalen.com/"),
    ("Venable Durham Apartments", 8.5, "$$$$", 35.99116, -78.89859, "https://venableapartments.com/?utm_source=google+local&utm_medium=organic&utm_campaign=website+link"),
    ("West Village", 8.5, "$", 35.99812, -78.90726, "https://www.westvillageapts.com/?utm_source=google+local&utm_medium=organic&utm_campaign=website+link"),
    ("Whetstone", 8.8, "$$", 35.99515, -78.90739, "https://www.whetstoneapartments.com/?ilm=obl&utm_source=obl&utm_medium=organic")
]

# 添加物业点，每个点的弹出窗口显示三行信息（物业名称、评分、价格级别）
for prop in properties:
    name, rating, price, lat, lon, url = prop
    
    # 处理超链接
    if url:
        name_html = f'<a href="{url}" target="_blank">{name}</a>'
    else:
        name_html = name
    
    # 构造 HTML 内容
    html = f"<b>{name_html}</b><br>Rating: {rating}<br>Price Level: {price}"
    iframe = IFrame(html, width=250, height=80)
    popup = folium.Popup(iframe, max_width=250)
    
    # 添加标记
    folium.Marker(
        location=[lat, lon],
        popup=popup,
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# 保存地图为 HTML 文件
m.save('durham_map.html')
