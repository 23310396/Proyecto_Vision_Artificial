# Reporte de limpieza del dataset

## Criterio usado

Se conservaron únicamente las clases con al menos 10 anotaciones totales.

La razón es que las clases con 1, 2, 3 o muy pocas imágenes no aportan suficiente información para que YOLO aprenda de forma estable.

## Resumen

| Concepto | Cantidad |
|---|---:|
| Clases originales | 36 |
| Clases conservadas | 15 |
| Clases eliminadas | 21 |
| Imágenes conservadas | 427 |
| Anotaciones conservadas | 427 |

## Distribución final

| Split | Imágenes | Labels | Anotaciones |
|---|---:|---:|---:|
| Train | 344 | 344 | 344 |
| Valid | 41 | 41 | 41 |
| Test | 42 | 42 | 42 |

## Clases conservadas

| ID nuevo | ID original | Marca | Anotaciones |
|---:|---:|---|---:|
| 0 | 1 | audi | 15 |
| 1 | 5 | chevrolet | 14 |
| 2 | 6 | citroen | 17 |
| 3 | 7 | dacia | 20 |
| 4 | 12 | ford | 16 |
| 5 | 15 | hyundai | 24 |
| 6 | 21 | mercedes | 10 |
| 7 | 23 | nissan | 14 |
| 8 | 25 | peugeot | 63 |
| 9 | 27 | renault | 90 |
| 10 | 28 | seat | 24 |
| 11 | 29 | skoda | 16 |
| 12 | 30 | suzuki | 32 |
| 13 | 32 | toyota | 10 |
| 14 | 33 | volkswagen | 62 |

## Clases eliminadas

| ID original | Marca | Anotaciones |
|---:|---|---:|
| 0 | Mitsubishi | 1 |
| 2 | brilliance | 3 |
| 3 | byd | 5 |
| 4 | chery | 1 |
| 8 | daewoo | 2 |
| 9 | daihatsu | 2 |
| 10 | dfsk | 1 |
| 11 | fiat | 4 |
| 13 | hafei | 1 |
| 14 | honda | 1 |
| 16 | jmc | 2 |
| 17 | kia | 9 |
| 18 | land rover | 1 |
| 19 | lifan | 1 |
| 20 | mazda | 2 |
| 22 | mini | 1 |
| 24 | opel | 9 |
| 26 | range rover | 2 |
| 31 | tata | 2 |
| 34 | yuejin | 2 |
| 35 | zotye | 1 |
