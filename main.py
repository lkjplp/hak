import uvicorn
from fastapi import FastAPI, Response
from starlette.middleware.cors import CORSMiddleware
import os

#!!!данные взяты из файла analitika.ipynb
data_year_user = [
  {"name":"2022Q1","loyl_din":0.0,"pmnts_nmbr_din":0.0,"pmnts_sum_din":0.0,"loyl":100.0,"pmnts_nmbr":11.8021201413,"pmnts_sum":45502.4400212014},
    {"name":"2022Q2","loyl_din":0.0,"pmnts_nmbr_din":-1.2105552456,"pmnts_sum_din":-5.3363159799,"loyl":100.0,"pmnts_nmbr":11.6592489569,"pmnts_sum":43074.2860431154},
    {"name":"2022Q3","loyl_din":0.0,"pmnts_nmbr_din":-1.1526220851,"pmnts_sum_din":10.2180183998,"loyl":100.0,"pmnts_nmbr":11.5248618785,"pmnts_sum":47475.6245165746},
    {"name":"2022Q4","loyl_din":0.0,"pmnts_nmbr_din":-2.8632012441,"pmnts_sum_din":-5.4093560349,"loyl":100.0,"pmnts_nmbr":11.1948818898,"pmnts_sum":44907.4989566929}
]

data_10years_user = [
{"name":2023.0,"loyl_din":0.0,"pmnts_nmbr_din":0.0,"pmnts_sum_din":0.0,"loyl":97.6653696498,"pmnts_nmbr":7.6387159533,"pmnts_sum":10091.1610058366},
    {"name":2024.0,"loyl_din":0.4118790538,"pmnts_nmbr_din":-4.7127422743,"pmnts_sum_din":29.318935093,"loyl":98.0676328502,"pmnts_nmbr":7.2787229574,"pmnts_sum":13049.7819512707},
    {"name":2025.0,"loyl_din":0.2585307972,"pmnts_nmbr_din":-5.3861663308,"pmnts_sum_din":-1.3270301336,"loyl":98.3211678832,"pmnts_nmbr":6.8866788321,"pmnts_sum":12876.6074124088},
    {"name":2026.0,"loyl_din":-0.0787431752,"pmnts_nmbr_din":7.9128668701,"pmnts_sum_din":34.2373108592,"loyl":98.2437466738,"pmnts_nmbr":7.4316125599,"pmnts_sum":17285.2115203122},
    {"name":2027.0,"loyl_din":-0.3047003426,"pmnts_nmbr_din":12.8288664775,"pmnts_sum_din":30.1403120671,"loyl":97.9443976411,"pmnts_nmbr":8.3850042123,"pmnts_sum":22495.0282139848},
    {"name":2028.0,"loyl_din":0.5428602193,"pmnts_nmbr_din":5.1019241832,"pmnts_sum_din":13.1485139268,"loyl":98.476098813,"pmnts_nmbr":8.81280077,"pmnts_sum":25452.7901315367},
    {"name":2029.0,"loyl_din":0.8083718744,"pmnts_nmbr_din":1.6914749638,"pmnts_sum_din":18.5709019139,"loyl":99.2721518987,"pmnts_nmbr":8.9618670886,"pmnts_sum":30179.6028212025},
    {"name":2030.0,"loyl_din":-0.855711277,"pmnts_nmbr_din":-12.8589622075,"pmnts_sum_din":1.5825352825,"loyl":98.4226689001,"pmnts_nmbr":7.8094639866,"pmnts_sum":30657.2056839754},
    {"name":2031.0,"loyl_din":-0.1853998248,"pmnts_nmbr_din":6.3170815681,"pmnts_sum_din":2.7288299229,"loyl":98.2401934444,"pmnts_nmbr":8.3027941967,"pmnts_sum":31493.7886861902},
    {"name":2032.0,"loyl_din":0.8302106484,"pmnts_nmbr_din":38.9779816369,"pmnts_sum_din":43.6405635931,"loyl":99.0557939914,"pmnts_nmbr":11.539055794,"pmnts_sum":45237.8555656652}
]

history_data_user = [
{"name":2013.0,"loyl_din":0.0,"pmnts_nmbr_din":0.0,"pmnts_sum_din":0.0,"loyl":97.6653696498,"pmnts_nmbr":7.6387159533,"pmnts_sum":10091.1610058366},
    {"name":2014.0,"loyl_din":0.4118790538,"pmnts_nmbr_din":-4.7127422743,"pmnts_sum_din":29.318935093,"loyl":98.0676328502,"pmnts_nmbr":7.2787229574,"pmnts_sum":13049.7819512707},
    {"name":2015.0,"loyl_din":0.2585307972,"pmnts_nmbr_din":-5.3861663308,"pmnts_sum_din":-1.3270301336,"loyl":98.3211678832,"pmnts_nmbr":6.8866788321,"pmnts_sum":12876.6074124088},
    {"name":2016.0,"loyl_din":-0.0787431752,"pmnts_nmbr_din":7.9128668701,"pmnts_sum_din":34.2373108592,"loyl":98.2437466738,"pmnts_nmbr":7.4316125599,"pmnts_sum":17285.2115203122},
    {"name":2017.0,"loyl_din":-0.3047003426,"pmnts_nmbr_din":12.8288664775,"pmnts_sum_din":30.1403120671,"loyl":97.9443976411,"pmnts_nmbr":8.3850042123,"pmnts_sum":22495.0282139848},
    {"name":2018.0,"loyl_din":0.5428602193,"pmnts_nmbr_din":5.1019241832,"pmnts_sum_din":13.1485139268,"loyl":98.476098813,"pmnts_nmbr":8.81280077,"pmnts_sum":25452.7901315367},
    {"name":2019.0,"loyl_din":0.8083718744,"pmnts_nmbr_din":1.6914749638,"pmnts_sum_din":18.5709019139,"loyl":99.2721518987,"pmnts_nmbr":8.9618670886,"pmnts_sum":30179.6028212025},
    {"name":2020.0,"loyl_din":-0.855711277,"pmnts_nmbr_din":-12.8589622075,"pmnts_sum_din":1.5825352825,"loyl":98.4226689001,"pmnts_nmbr":7.8094639866,"pmnts_sum":30657.2056839754},
    {"name":2021.0,"loyl_din":-0.1853998248,"pmnts_nmbr_din":6.3170815681,"pmnts_sum_din":2.7288299229,"loyl":98.2401934444,"pmnts_nmbr":8.3027941967,"pmnts_sum":31493.7886861902},
    {"name":2022.0,"loyl_din":0.8302106484,"pmnts_nmbr_din":38.9779816369,"pmnts_sum_din":43.6405635931,"loyl":99.0557939914,"pmnts_nmbr":11.539055794,"pmnts_sum":45237.8555656652}
]

data_year = [
  {"name":"2022Q1","loyl_din":0.0,"pmnts_nmbr_din":0.0,"pmnts_sum_din":0.0,"loyl":100.0,"pmnts_nmbr":16700,"pmnts_sum":64385952.6300000027},
    {"name":"2022Q2","loyl_din":0.0,"pmnts_nmbr_din":0.3952095808,"pmnts_sum_din":-3.7976129887,"loyl":100.0,"pmnts_nmbr":16766,"pmnts_sum":61940823.3299999982},
    {"name":"2022Q3","loyl_din":0.0,"pmnts_nmbr_din":-0.4652272456,"pmnts_sum_din":10.9844858434,"loyl":100.0,"pmnts_nmbr":16688,"pmnts_sum":68744704.299999997},
    {"name":"2022Q4","loyl_din":0.0,"pmnts_nmbr_din":2.2351390221,"pmnts_sum_din":-0.4446537273,"loyl":100.0,"pmnts_nmbr":17061,"pmnts_sum":68439028.4099999964}
]

data_10years = [
{"name":2023.0,"loyl_din":0.0,"pmnts_nmbr_din":0.0,"pmnts_sum_din":0.0,"loyl":97.6653696498,"pmnts_nmbr":39263.0,"pmnts_sum":51868567.5700000003},
{"name":2024.0,"loyl_din":0.4118790538,"pmnts_nmbr_din":-11.7387871533,"pmnts_sum_din":19.7835505794,"loyl":98.0676328502,"pmnts_nmbr":34654.0,"pmnts_sum":62130011.8699999973},
    {"name":2025.0,"loyl_din":0.2585307972,"pmnts_nmbr_din":8.9022912218,"pmnts_sum_din":13.5744328645,"loyl":98.3211678832,"pmnts_nmbr":37739.0,"pmnts_sum":70563808.6200000048},
    {"name":2026.0,"loyl_din":-0.0787431752,"pmnts_nmbr_din":11.0045311217,"pmnts_sum_din":38.0831608236,"loyl":98.2437466738,"pmnts_nmbr":41892.0,"pmnts_sum":97436737.3400000036},
    {"name":2027.0,"loyl_din":-0.3047003426,"pmnts_nmbr_din":18.7935644037,"pmnts_sum_din":37.020179549,"loyl":97.9443976411,"pmnts_nmbr":49765.0,"pmnts_sum":133507992.450000003},
    {"name":2028.0,"loyl_din":0.5428602193,"pmnts_nmbr_din":10.3968652668,"pmnts_sum_din":18.8488350159,"loyl":98.476098813,"pmnts_nmbr":54939.0,"pmnts_sum":158672693.6800000072},
    {"name":2029.0,"loyl_din":0.8083718744,"pmnts_nmbr_din":3.0943409964,"pmnts_sum_din":20.2066249752,"loyl":99.2721518987,"pmnts_nmbr":56639.0,"pmnts_sum":190735089.8300000131},
    {"name":2030.0,"loyl_din":-0.855711277,"pmnts_nmbr_din":-1.2217729833,"pmnts_sum_din":15.1483042348,"loyl":98.4226689001,"pmnts_nmbr":55947.0,"pmnts_sum":219628221.5200000107},
    {"name":2031.0,"loyl_din":-0.1853998248,"pmnts_nmbr_din":10.4724113894,"pmnts_sum_din":6.7439154028,"loyl":98.2401934444,"pmnts_nmbr":61806.0,"pmnts_sum":234439762.9799999893},
    {"name":2032.0,"loyl_din":0.8302106484,"pmnts_nmbr_din":8.7515775167,"pmnts_sum_din":12.4000917423,"loyl":99.0557939914,"pmnts_nmbr":67215.0,"pmnts_sum":263510508.6699999869}
]

history_data = [
{"name":2013.0,"loyl_din":0.0,"pmnts_nmbr_din":0.0,"pmnts_sum_din":0.0,"loyl":97.6653696498,"pmnts_nmbr":39263.0,"pmnts_sum":51868567.5700000003},
{"name":2014.0,"loyl_din":0.4118790538,"pmnts_nmbr_din":-11.7387871533,"pmnts_sum_din":19.7835505794,"loyl":98.0676328502,"pmnts_nmbr":34654.0,"pmnts_sum":62130011.8699999973},
    {"name":2015.0,"loyl_din":0.2585307972,"pmnts_nmbr_din":8.9022912218,"pmnts_sum_din":13.5744328645,"loyl":98.3211678832,"pmnts_nmbr":37739.0,"pmnts_sum":70563808.6200000048},
    {"name":2016.0,"loyl_din":-0.0787431752,"pmnts_nmbr_din":11.0045311217,"pmnts_sum_din":38.0831608236,"loyl":98.2437466738,"pmnts_nmbr":41892.0,"pmnts_sum":97436737.3400000036},
    {"name":2017.0,"loyl_din":-0.3047003426,"pmnts_nmbr_din":18.7935644037,"pmnts_sum_din":37.020179549,"loyl":97.9443976411,"pmnts_nmbr":49765.0,"pmnts_sum":133507992.450000003},
    {"name":2018.0,"loyl_din":0.5428602193,"pmnts_nmbr_din":10.3968652668,"pmnts_sum_din":18.8488350159,"loyl":98.476098813,"pmnts_nmbr":54939.0,"pmnts_sum":158672693.6800000072},
    {"name":2019.0,"loyl_din":0.8083718744,"pmnts_nmbr_din":3.0943409964,"pmnts_sum_din":20.2066249752,"loyl":99.2721518987,"pmnts_nmbr":56639.0,"pmnts_sum":190735089.8300000131},
    {"name":2020.0,"loyl_din":-0.855711277,"pmnts_nmbr_din":-1.2217729833,"pmnts_sum_din":15.1483042348,"loyl":98.4226689001,"pmnts_nmbr":55947.0,"pmnts_sum":219628221.5200000107},
    {"name":2021.0,"loyl_din":-0.1853998248,"pmnts_nmbr_din":10.4724113894,"pmnts_sum_din":6.7439154028,"loyl":98.2401934444,"pmnts_nmbr":61806.0,"pmnts_sum":234439762.9799999893},
    {"name":2022.0,"loyl_din":0.8302106484,"pmnts_nmbr_din":8.7515775167,"pmnts_sum_din":12.4000917423,"loyl":99.0557939914,"pmnts_nmbr":67215.0,"pmnts_sum":263510508.6699999869}
]

ext_data = [
{
  "id1": 1,
   "id2": 2,
   "id3": 3,
   "id4": 4,
   "id5": 5,
   "val1": 4,
    "val2": 2,
    "val3": 2,
    "val4": 2,
    "val5": 2
}
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/model_10_years/")
async def read_root(user_id : str, val1_infl : float, val2_bez : float, val3_klst : float, val4_vvp : float):
    model(val1_infl, val2_bez, val3_klst, val4_vvp)
    if user_id == '0':
        return data_10years
    else:
        return data_10years_user

@app.post("/model_year/")
async def read_root(user_id : str, val1_infl : float, val2_bez : float, val3_klst : float, val4_vvp : float):
    model(val1_infl, val2_bez, val3_klst, val4_vvp)
    if user_id == '0':
        return data_year
    else:
        return data_year_user

@app.post("/model_history_data/")
async def read_root(user_id : str, val1_infl : float, val2_bez : float, val3_klst : float, val4_vvp : float):
    model(val1_infl, val2_bez, val3_klst, val4_vvp)
    if user_id == '0':
        return history_data
    else:
        return history_data_user


@app.post("/ext_data/")
async def read_root():
    return ext_data



@app.delete("/")
async def kill():
    os.kill(os.getpid(), 9)
    return {"message": "error"}


if __name__ == "__main__":
    uvicorn.run(app , port=8000)
    #uvicorn.run(app, host='0.0.0.0' , port=8000)
