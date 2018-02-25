'''import pandas as pd
import matplotlib.pyplot as plt


def data_plot():
    """ç»å¶ç¨æ·å­¦ä¹ æ°æ®å¾å½¢
    """

    df = pd.read_json('user_study.json')

    data = df.groupby('user_id').sum().head(100)

    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
    ax.set_title('StudyData')
    ax.plot(data.index, data.minutes)
    plt.show()

if __name__ == '__main__':
    data_plot()

    '''

import pandas as pd
from matplotlib import pyplot as plt

def data_plot():
    data=pd.read_json('user_study.json')
    userdata=data.groupby('user_id').minutes.sum().head(100)
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.set_xlabel('User Id')
    ax.set_ylabel('Study Time')
    ax.set_title('Study Data')
    ax.plot(userdata.index, userdata.data)
    plt.show()

if __name__=='__main__':
    data_plot()
