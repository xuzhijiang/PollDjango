## Start

language字段指定了默认运行环境，这里设定使用 Python 环境:

`language: python`

需要sudo:

`sudo: required`

在安装依赖之前需要安装foo模块，然后执行脚本py.test:

```shell
before_install: sudo pip install foo
script: py.test
```

## 运行流程

* install 阶段：安装依赖
* script 阶段：运行脚本

### install 字段

`install`字段用来指定安装脚本:

```shell
install: ./install-dependencies.sh
```

如果有多个脚本，可以写成下面的形式:

```shell
install:
  - command1
  - command2
```

如果command1失败了，整个构建就会停下来，不再往下进行,如果不需要安装，即跳过安装阶段，就直接设为true。

```shell
install: true
```

script字段用来指定构建或测试脚本:

`script: bundle exec thor build`


如果有多个脚本，可以写成下面的形式。

```shell
script:
  - command1
  - command2
```

注意，script与install不一样，如果command1失败，command2会继续执行。但是，整个构建阶段的状态是失败。

如果command2只有在command1成功后才能执行，就要写成下面这样。

`script: command1 && command2`

`script: true`表示不执行任何脚本，状态直接设为成功

### 7个钩子

* before_install：install 阶段之前执行
* before_script：script 阶段之前执行
* after_failure：script 阶段失败时执行
* after_success：script 阶段成功时执行
* before_deploy：deploy 步骤之前执行
* after_deploy：deploy 步骤之后执行
* after_script：script 阶段之后执行

### 完整的生命周期

1. before_install
2. install
3. before_script
4. script
5. aftersuccess or afterfailure
6. [OPTIONAL] before_deploy
7. [OPTIONAL] deploy
8. [OPTIONAL] after_deploy
9. after_script

### 运行状态

Travis 每次运行，可能会返回四种状态:

* passed：运行成功，所有步骤的退出码都是0
* canceled：用户取消执行
* errored：before_install、install、before_script有非零退出码，运行会立即停止
* failed ：script有非零状态码 ，会继续运行

### 环境变量

`.travis.yml`的`env`字段可以定义环境变量。
