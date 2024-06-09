# Python Test Assignment with Playwright for myTomorrows
## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Running Tests](#running-tests)
- [Allure Report](#allure-report)


## Introduction

This document provides step-by-step instructions on launching the tests with Allure and Playwright.

## Prerequisites

Before getting started, make sure you have the following prerequisites installed:

- [Python 3.x](https://www.python.org/downloads/)
- PIP
 ```shell
    python3 -m ensurepip
```
- venv
 ```shell
    pip install virtualenv
```

## Getting Started

To get started with Python and Playwright, follow these steps:

1. Clone or download this repository.
2. Open a terminal and navigate to the project directory.
3. Create and activate an isolated environment by running the following commands
```shell
python3 -m venv venv
```
For Linux & Mac run 
```shell
source venv/bin/activate
```
For Windows run
```shell
venv\Scripts\activate.ps1
```
4. Install the project dependencies by running the following command:
```shell
pip3 install -r requirements.txt
```

## Running Tests

Running tests using Playwright in headless mode

```shell
python3 -m pytest -s tests --screenshot on --verbose
```

Running tests using Playwright in headed mode
```shell
python3 -m pytest -s tests --screenshot on --verbose --headed
```
Running tests in headed mode & specific browser(chromium,firefox)

```shell
python3 -m pytest -s tests --browser firefox  --screenshot on --verbose --headed
```


## Allure Report
To generate HTML report using Allure reporting framework run tests with `--alluredir` parameter

```shell
python3 -m pytest -s --alluredir=allure-results tests --numprocesses auto --browser chromium --browser firefox  --screenshot on --video on --headed --verbose
```

And generate and open report in browser by running
```shell
allure serve -h localhost
```
