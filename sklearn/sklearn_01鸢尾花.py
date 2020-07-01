# sklearn_01鸢尾花.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer


# sklearn数据集的使用
def datasets_demo():
	iris = load_iris()
	print("鸢尾花数据集的返回值：n",iris)
	print("查看数据集描述: \n",iris["DESCR"])
	print("查看特征值的名字 \n",iris.feature_name)
	print("查看特征值：\n",iris.data,iris.data.shape)
	return None



def dict_demo():
	"""
	字典特征提取
	"""
	data = [{"city":"北京",'temperature':100},{"city":"上海",'temperature':60},{"city":"广州",'temperature':30}]
	transfer = DictVectorizer(sparse=False)
	transfer1 = DictVectorizer(sparse=True)

	data_new = transfer.fit_transform(data)
	data_new1 = transfer1.fit_transform(data)

	print("data_new:\n",data_new)
	print("data_new1:\n",data_new1)
	print("特征名字：\n",transfer.get_feature_names())
	return None

if __name__ == '__main__':
	# 代码1：sklearn数据集的使用（鸢yuan尾花数据集)
	# datasets_demo()
	dict_demo()