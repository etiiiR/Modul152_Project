# Modul152_Project
This is a Project Repository for the Modul 152 
Package: Python 3.7
         Django
         Django REST
         Vue.js 2.12
         Docker
         
Docker command : 

```docker
build -t music4you .
```
```docker
docker run -p 8001:8001 music4you
```

# vue-django-webpack-boilerplate

## HOW to Start
cd music4you




<p align="center">
  <b>Listed in</b>
  <br>
  <a href="https://github.com/vuejs/awesome-vue#scaffold" target="_blank"><img src="https://github.com/vuejs/awesome-vue/raw/master/logo.svg?sanitize=true" align="center" height="150" alt="Awesome VueJS"></a>
</p>

> A full-featured Webpack setup with hot-reload, lint-on-save, unit testing & css extraction integrated into a django application

## Vue CLI Version Notice

If you are using `vue-cli@1.x`, it will be pulling the `master` branch of this template by default. If you are using `vue-cli@2.x`, it will be pulling the `dist` branch instead, which provides more configurable options thanks to new features in `vue-cli@2.x`. It is recommended to upgrade `vue-cli` as soon as you can.

## VueJS Templates Documentation

Common topics are discussed in the [docs](http://vuejs-templates.github.io/webpack). Make sure to read it!

# Vue Django
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![Help Contribute to Open Source](https://www.codetriage.com/ndagistanley/vue-django/badges/users.svg)](https://www.codetriage.com/ndagistanley/vue-django)

[![Build Status](https://semaphoreci.com/api/v1/stanmd/vue-django/branches/develop/badge.svg)](https://semaphoreci.com/stanmd/vue-django)
[![Updates](https://pyup.io/repos/github/NdagiStanley/vue-django/shield.svg)](https://pyup.io/repos/github/NdagiStanley/vue-django/)
[![Python 3](https://pyup.io/repos/github/NdagiStanley/vue-django/python-3-shield.svg)](https://pyup.io/repos/github/NdagiStanley/vue-django/)

[https://vuedjango.herokuapp.com/](https://vuedjango.herokuapp.com/) is a deployed instance of this boilerplate.

[Vue-Django Docs](https://ndagistanley.github.io/vue-django/) offer a more comprehensive documentation.

## Usage of VueDjango

This is a project template that includes `VueJS` and `Django` based on the [vue-cli](https://github.com/vuejs/vue-cli) templates. **It is recommended to use npm 3+ for a more efficient dependency tree.**

``` bash
$ npm install -g vue-cli
```
You might want to use ```sudo``` if you encounter permissions error
```bash
$ vue init NdagiStanley/vue-django my-project
$ cd my-project
$ npm install
```

Secondly, have *Python* installed and preferably create a virtual environment for the project.

To develop

```bash
$ npm run dev
```

## Deploy
To deploy your django project, still within `my-project` directory, run:

`$ .deploy.sh`

Then get to [localhost:8000](http://localhost:8000/). You should have a page exactly like the image below or as the deployed instance mentioned earlier: [https://vuedjango.herokuapp.com/](https://vuedjango.herokuapp.com/)

<p align="center">
  <img src="http://i.imgur.com/sY3IpBE.png?1" align="center" height="500" alt="Vue-Django">
</p>

> Docker

##### Ensure that **docker** is running.

If you use `docker` in your workflow, there is a `Dockerfile` in the root directory for you. Simply run
```
docker build -t [image-name] .
```
Use your preferred _image name_ in place of the `image-name` in the command. Remember to enter the trailing period before running it.

There is a docker container for vue-django that you can run. Simply run the following command.
```bash
docker run -p 8000:8000 stanmd/vue-django
```

Then get to [localhost:8000](http://localhost:8000/). You should have a page exactly like the image above

## What's Included

- `npm run dev`: first-in-class development experience.
  - Webpack + `vue-loader` for single file Vue components.
  - State preserving hot-reload
  - State preserving compilation error overlay
  - Lint-on-save with ESLint
  - Source maps

- `npm run build`: Production ready build.
  - JavaScript minified with [UglifyJS](https://github.com/mishoo/UglifyJS2).
  - HTML minified with [html-minifier](https://github.com/kangax/html-minifier).
  - CSS across all components extracted into a single file and minified with [cssnano](https://github.com/ben-eb/cssnano).
  - All static assets compiled with version hashes for efficient long-term caching, and a production `index.html` is auto-generated with proper URLs to these generated assets.

- `npm run unit`: Unit tests run in PhantomJS with [Karma](http://karma-runner.github.io/0.13/index.html) + [Mocha](http://mochajs.org/) + [karma-webpack](https://github.com/webpack/karma-webpack).
  - Supports ES2015 in test files.
  - Supports all webpack loaders.
  - Easy mock injection.

- `npm run e2e`: End-to-end tests with [Nightwatch](http://nightwatchjs.org/).
  - Run tests in multiple browsers in parallel.
  - Works with one command out of the box:
    - Selenium and chromedriver dependencies automatically handled.
    - Automatically spawns the Selenium server.

### Contributions

**NB**: This repo has been forked from vue-webpack-boilerplate to help you start a Django application utilizing the awesomeness of `Vue JS` and `vue-cli`

Feel free to contribute to this repo.

To create your own boilerplate, fork this repo or [vue-webpack-boilerplate](https://github.com/vuejs-templates/webpack) and use it with `vue-cli`:

``` bash
vue init username/repo my-project
```
