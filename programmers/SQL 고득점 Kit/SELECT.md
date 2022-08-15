# SELECT
[link](https://school.programmers.co.kr/learn/courses/30/parts/17042)

**모든 레코드 조회하기**

```sql
SELECT * FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

**역순 정렬하기**

```sql
SELECT NAME, DATETIME FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC
```

**아픈 동물 찾기**

```sql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
```

**어린 동물 찾기**

```sql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE INTAKE_CONDITION != "Aged"
```