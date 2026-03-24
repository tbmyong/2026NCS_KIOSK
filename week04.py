import seaborn as sns
#유럽 제조 차량중 연비가 30.0 mpg이상인 행 추출하시오
#단, 자동차 모델명, 연비, 제조국가만 표시하고 연비가 높은 순으로 정렬하시오

mpg = sns.load_dataset('mpg')
#print(mpg)
#print(mpg.iat[1,8])
#print(mpg[['origin','mpg','name']])
#print(mpg[['origin','mpg','name']].query('origin == "europe" and mpg >30.0')) #이렇게 하면 europe에서 key값 missing
print(mpg[['origin','mpg','name']].query('origin == "europe" and mpg >30.0').sort_values('mpg', ascending=False))

