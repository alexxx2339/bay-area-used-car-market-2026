library(chromote)
library(rvest)
library(dplyr)
library(stringr)


b <- ChromoteSession$new()
url <- "https://www.cargurus.com/search?sourceContext=cargurus&sortType=BEST_MATCH&sortDirection=ASC&distance=50&newUsed=2&isDeliveryEnabled=false&hideWithoutPhotos=false&seoPageTypeId=10&srpVariation=DEFAULT_SEARCH"

b$Page$navigate(url)

Sys.sleep(10)

html <- b$Runtime$evaluate(
  "document.documentElement.outerHTML"
)$result$value


page_live <- read_html(html)



page_live %>%
  html_text2() %>%
  str_detect("Cadillac Escalade")


library(reticulate)

py_config()

py_install("playwright")
py_install("pandas")

py_run_string("
import sys
print(sys.version)
import pandas as pd
print('pandas works')
")



py_run_string("
import subprocess, sys
subprocess.run([sys.executable, '-m', 'playwright', 'install', 'chromium'])
")

py_run_string("
import pandas as pd
print('pandas loaded')
")
py_run_string("
import subprocess, sys
subprocess.run([sys.executable, '-m', 'playwright', 'install', 'chromium'])
")

library(readr)

cars <- read_csv("data/craigslist_cars_sample.csv")

nrow(cars)
ncol(cars)

glimpse(cars)





