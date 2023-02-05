import warnings
from pprint import pprint
from glob import glob

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def File_Path(
    data_path: str = "../data/",
    file_format: list = [".parquet"],
    file_list: list = ["esgRating", "stockPrice", "finaStat", "indexPrice"],
):

    globals()["data_path"] = "../data/"
    global fp
    fp = {}
    if len(file_format) == 1:
        file_format = file_format * len(file_list)

    for fn, ff in zip(file_list, file_format):
        fp[fn] = f"{data_path}{fn}{ff}"

    print(f"data_path : {data_path}")
    print("fp")
    pprint(fp)


File_Path()


def six_digit(x):
    if pd.isna(x) == True:
        pass
    else:
        return "%06d" % x


def DerivedCol_Date(df, col_YMD="연_월_일", col_deri=["연", "분기", "월", "일"], inplace=False, Sep="-"):

    if inplace:
        df_ = df
        print("inplace :", inplace)
    else:
        df_ = df.copy()

    if df_[col_YMD].dtypes != "datetime64[ns]":
        df_[col_YMD] = pd.to_datetime(df_[col_YMD])

    with warnings.catch_warnings(record=False):
        if inplace:
            warnings.simplefilter("ignore")

        df_[col_deri[0]] = df_[col_YMD].dt.year
        df_[col_deri[1]] = df_[col_YMD].dt.quarter
        df_[col_deri[2]] = df_[col_YMD].dt.month

        sY = df_[col_deri[0]].astype("str")
        sQ = df_[col_deri[1]].astype("str")
        sM = df_[col_deri[2]].astype("str")

        df_[f"{col_deri[0]}_{col_deri[1]}"] = sY + Sep + sQ
        df_[f"{col_deri[0]}_{col_deri[2]}"] = sY + Sep + sM
        df_[f"{col_deri[1]}_{col_deri[2]}"] = sQ + Sep + sM

        df_[f"{col_deri[0]}_{col_deri[1]}_{col_deri[2]}"] = sY + Sep + sQ + Sep + sM

        if col_YMD == "연_월_일":
            df_[col_deri[3]] = df_[col_YMD].dt.day
            sD = df_[col_deri[3]].astype("str")
            df_[f"{col_deri[2]}_{col_deri[3]}"] = sM + Sep + sD

    return df_


def DerivedCol_Groupby_MinMaxScaler(
    df: pd.DataFrame, col_groupby: list, col_mmScl: list, inplace=False
):
    """
    refer : https://stackoverflow.com/questions/69476352/sklearn-minmaxscaler-with-groupby-pandas
    """
    from sklearn.preprocessing import MinMaxScaler

    if inplace:
        df_ = df
        print("inplace :", inplace)
    else:
        df_ = df.copy()

    def agg(x):

        col_name = []
        for i in col_mmScl:
            col_name.append(f"{i}_mmscl")

        scaler = MinMaxScaler()
        x[col_name] = scaler.fit_transform(x[col_mmScl])

        return x

    with warnings.catch_warnings(record=False):
        if inplace:
            warnings.simplefilter("ignore")

        df_ = df_.groupby(col_groupby).apply(agg)

    return df_


def print_title(body, br=2, bp="┌▣ ", hr=" ---- ---- ---- ----"):

    """
    body : 내용
    bp : bullet point, 글머리 기호
    hr : Horizontal Rule, 수평선
    """

    class ff:
        PURPLE = "\033[95m"
        CYAN = "\033[96m"
        DARKCYAN = "\033[36m"
        BLUE = "\033[94m"
        GREEN = "\033[92m"
        YELLOW = "\033[93m"
        RED = "\033[91m"
        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"
        END = "\033[0m"

    print("\n" * br + ff.BOLD + bp + ff.UNDERLINE + body + ff.END + hr)


def Check_df(df):

    print_title("""df.shape""")
    print(df.shape)

    print_title("""df.info()""")
    print(df.info())

    print_title("""df.head()""")
    display(df.head())

    print_title("""df.columns.to_list()""")
    print(df.columns.to_list())


def Summary_df(df):

    print_title("""df.describe().T""")
    display(df.describe().T)

    try:
        print_title("""df.describe(include=['O'])""")
        display(df.describe(include=["O"]))
    except:
        pass

    # 결측치
    df_temp = df.isna()
    print_title("""df.isna().sum()""")
    display(df_temp.sum().to_frame())

    print_title("""sns.heatmap(data=df.isna())""")
    sns.heatmap(data=df.isna(), cmap="Greys")
    plt.title("""sns.heatmap(data=df.isna())""", fontsize=20)
    plt.show()

    print_title("df.isna().mean()")
    display(df_temp.mean().to_frame())


def reduce_mem_usage(df: pd.DataFrame, verbose: bool = True, to_num: bool or list = False):
    numerics = [
        "uint16",
        "uint32",
        "uint64",
        "int16",
        "int32",
        "int64",
        "float16",
        "float32",
        "float64",
    ]
    start_mem = df.memory_usage().sum() / 1024**2

    if to_num != False:
        list_toNumErr = []

        if to_num == True:
            to_num = df.columns.to_list()

        for i in to_num:
            try:
                df[i] = pd.to_numeric(df[i])
            except:
                list_toNumErr.append(i)

    for col in df.columns:
        col_type = df[col].dtypes

        if col_type in numerics:
            c_min = df[col].min()
            c_max = df[col].max()

            if str(col_type)[:3] == "int" or str(col_type)[:4] == "uint":
                # uint
                if c_min >= 0:
                    if c_min > np.iinfo(np.uint8).min and c_max < np.iinfo(np.uint8).max:
                        df[col] = df[col].astype(np.uint8)
                    elif c_min > np.iinfo(np.uint16).min and c_max < np.iinfo(np.uint16).max:
                        df[col] = df[col].astype(np.uint16)
                    elif c_min > np.iinfo(np.uint32).min and c_max < np.iinfo(np.uint32).max:
                        df[col] = df[col].astype(np.uint32)
                    elif c_min > np.iinfo(np.uint64).min and c_max < np.iinfo(np.uint64).max:
                        df[col] = df[col].astype(np.uint64)

                # int
                else:
                    if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                        df[col] = df[col].astype(np.int8)
                    elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                        df[col] = df[col].astype(np.int16)
                    elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                        df[col] = df[col].astype(np.int32)
                    elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                        df[col] = df[col].astype(np.int64)

            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)

    end_mem = df.memory_usage().sum() / 1024**2

    if verbose:
        print(
            "Mem. usage decreased to {:5.2f} Mb ({:.1f}% reduction)".format(
                end_mem, 100 * (start_mem - end_mem) / start_mem
            )
        )
        if to_num != False:
            print(list_toNumErr)

    return df


def DataLoad(file: str):
    """
    데이터를불러올 때 사용할 함수
    csv 포맷의 데이터의 경우 단순한한 전처리를 실행함.
    """
    fd = "/".join(file.split("/")[:-1])
    fn = "".join(file.split("/")[-1].split(".")[:-1])
    ff = file.split("/")[-1].split(".")[-1]

    if glob(f"{file}"):

        if "parquet" == ff:
            df = reduce_mem_usage(pd.read_parquet(file))

        if "pickle" == ff:
            df = reduce_mem_usage(pd.read_pickle(file))

        if "csv" == ff:

            try:
                df = reduce_mem_usage(pd.read_csv(file, index_col=False))
            except:
                df = reduce_mem_usage(pd.read_csv(file, index_col=False, encoding="cp949"))

            pp = {
                "종목코드": ".apply(six_digit)",
                "stock_code": ".apply(six_digit)",
            }

            col = df.columns.to_list()
            for i in pp.keys():
                if i in col:
                    e = f"""df["{i}"]{pp[i]}"""
                    print(e)
                    df[i] = eval(e)

        Check_df(df)

        return df

    else:
        raise Exception("file not found")


def DfPrst(df: pd.DataFrame, file: str = "../data/temp", *format: str):
    """
    df : pandas.DataFrame
    prst : persistence
    pd.df를 영속화하는 함수
    """

    # suport format list
    sl = ["csv", "pickle", "parquet"]

    # file dir
    fd = "/".join(file.split("/")[:-1])
    # file name
    fn = "".join(file.split("/")[-1].split(".")[:-1])
    # file format
    ff = file.split("/")[-1].split(".")[-1]

    # 만약 파일 이름에 포맷도 포함되어 있다면 제거하는 조건문
    if ff in sl:
        file = fd + "/" + fn
        format += (ff,)

    p = []

    if "csv" in format:
        f = file + ".csv"
        df.to_csv(f, index=False)
        p += glob(f)

    if "pickle" in format:
        f = file + ".pickle"
        df.to_pickle(f)
        p += glob(f)

    if "parquet" in format:
        f = file + ".parquet"
        df.to_parquet(f, index=False, engine="fastparquet")
        p += glob(f)

    pprint(p)
