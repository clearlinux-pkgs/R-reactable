#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-reactable
Version  : 0.3.0
Release  : 5
URL      : https://cran.r-project.org/src/contrib/reactable_0.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/reactable_0.3.0.tar.gz
Summary  : Interactive Data Tables Based on 'React Table'
Group    : Development/Tools
License  : MIT
Requires: R-digest
Requires: R-htmltools
Requires: R-htmlwidgets
Requires: R-jsonlite
Requires: R-reactR
BuildRequires : R-crosstalk
BuildRequires : R-digest
BuildRequires : R-htmltools
BuildRequires : R-htmlwidgets
BuildRequires : R-jsonlite
BuildRequires : R-reactR
BuildRequires : R-shiny
BuildRequires : buildreq-R

%description
JavaScript library. Provides an HTML widget that can be used in 'R Markdown'
    documents and 'Shiny' applications, or viewed from an R console.

%prep
%setup -q -c -n reactable
cd %{_builddir}/reactable

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653609168

%install
export SOURCE_DATE_EPOCH=1653609168
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reactable
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reactable
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reactable
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc reactable || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/reactable/DESCRIPTION
/usr/lib64/R/library/reactable/INDEX
/usr/lib64/R/library/reactable/LICENSE
/usr/lib64/R/library/reactable/Meta/Rd.rds
/usr/lib64/R/library/reactable/Meta/features.rds
/usr/lib64/R/library/reactable/Meta/hsearch.rds
/usr/lib64/R/library/reactable/Meta/links.rds
/usr/lib64/R/library/reactable/Meta/nsInfo.rds
/usr/lib64/R/library/reactable/Meta/package.rds
/usr/lib64/R/library/reactable/NAMESPACE
/usr/lib64/R/library/reactable/NEWS.md
/usr/lib64/R/library/reactable/R/reactable
/usr/lib64/R/library/reactable/R/reactable.rdb
/usr/lib64/R/library/reactable/R/reactable.rdx
/usr/lib64/R/library/reactable/examples/app/app.R
/usr/lib64/R/library/reactable/examples/app/assets/styles.css
/usr/lib64/R/library/reactable/examples/shiny-data-streaming.R
/usr/lib64/R/library/reactable/help/AnIndex
/usr/lib64/R/library/reactable/help/aliases.rds
/usr/lib64/R/library/reactable/help/figures/iris.png
/usr/lib64/R/library/reactable/help/paths.rds
/usr/lib64/R/library/reactable/help/reactable.rdb
/usr/lib64/R/library/reactable/help/reactable.rdx
/usr/lib64/R/library/reactable/html/00Index.html
/usr/lib64/R/library/reactable/html/R.css
/usr/lib64/R/library/reactable/htmlwidgets/reactable.js
/usr/lib64/R/library/reactable/htmlwidgets/reactable.js.map
/usr/lib64/R/library/reactable/htmlwidgets/reactable.yaml
/usr/lib64/R/library/reactable/htmlwidgets/reactable_v1.js
/usr/lib64/R/library/reactable/htmlwidgets/reactable_v1.js.LICENSE.txt
/usr/lib64/R/library/reactable/htmlwidgets/reactable_v1.js.map
/usr/lib64/R/library/reactable/tests/testthat.R
/usr/lib64/R/library/reactable/tests/testthat/test-columns.R
/usr/lib64/R/library/reactable/tests/testthat/test-language.R
/usr/lib64/R/library/reactable/tests/testthat/test-reactable.R
/usr/lib64/R/library/reactable/tests/testthat/test-shiny.R
/usr/lib64/R/library/reactable/tests/testthat/test-theme.R
/usr/lib64/R/library/reactable/tests/testthat/test-utils.R
