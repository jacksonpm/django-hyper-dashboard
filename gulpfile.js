var gulp = require('gulp'),
    uglify = require('gulp-uglify'),
    concat = require('gulp-concat');

gulp.task('js', function () {
   return gulp
      .src([
          'static/hyper/js/vendor.min.js',
          'static/hyper/js/app.min.js',
          'static/suit/js/suit.js',
          'static/hyper/js/alertas.js',
          'static/external/js/jquery.mask.js',
          'static/external/js/sweet.alert.js',
          'static/hyper/js/date-picker-br.js',
          'static/external/js/bootstrap-select.min.js',
          'static/hyper/js/jquery.validate.min.js',
          'static/hyper/js/utils.js',
      ])
      .pipe(concat('app.js'))
      .pipe(gulp.dest('hyper_dashboard/static/hyper/js'));
});

gulp.task('css', function () {
   return gulp
      .src([
          'static/hyper/css/toast.css',
          'static/hyper/css/style.css',
          'static/hyper/css/base-admin.css',
          'static/hyper/css/navbar.css',
          'static/external/css/material.icons.css',
          'static/external/css/bootstrap-select.min.css',
      ])
      .pipe(concat('app.css'))
      .pipe(gulp.dest('hyper_dashboard/static/hyper/css'));
});

