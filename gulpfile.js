var gulp = require('gulp'),
    uglify = require('gulp-uglify'),
    concat = require('gulp-concat');

gulp.task('js', function () {
   return gulp
      .src([
          'hyper_dashboard/static/hyper/js/vendor.min.js',
          'hyper_dashboard/static/hyper/js/hyper.min.js',
          'hyper_dashboard/static/suit/js/suit.js',
          'hyper_dashboard/static/hyper/js/alertas.js',
          'hyper_dashboard/static/external/js/jquery.mask.js',
          'hyper_dashboard/static/external/js/sweet.alert.js',
          'hyper_dashboard/static/hyper/js/date.picker.js',
          'hyper_dashboard/static/external/js/bootstrap-select.min.js',
          'hyper_dashboard/static/hyper/js/jquery.validate.min.js',
          'hyper_dashboard/static/hyper/js/utils.js',
      ])
      .pipe(concat('app.js'))
      .pipe(gulp.dest('hyper_dashboard/static/hyper/js'));
});

gulp.task('css', function () {
   return gulp
      .src([
          'hyper_dashboard/static/hyper/css/toast.css',
          'hyper_dashboard/static/hyper/css/style.css',
          'hyper_dashboard/static/hyper/css/base-admin.css',
          'hyper_dashboard/static/hyper/css/navbar.css',
          'hyper_dashboard/static/external/css/material.icons.css',
          'hyper_dashboard/static/external/css/bootstrap-select.min.css',
      ])
      .pipe(concat('app.css'))
      .pipe(gulp.dest('hyper_dashboard/static/hyper/css'));
});

