import numpy as np

# 行列の作成
a = np.array([[1,2,3], [4,5,6]])
print(a)#中身
print(type(a))#型
print(a.shape)#サイズ

#行
print(a[0])

#列の参照
print(a[:,0])

#行指定も可能
print(a[0:2])

#列の指定
print(a[:,0:2])

# 「行列 + 1」は全要素に対する和を実行
print(a + 1)

#行列演算ではない！
print(a * a)
