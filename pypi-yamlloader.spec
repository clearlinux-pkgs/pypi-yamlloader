#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-yamlloader
Version  : 1.3.2
Release  : 30
URL      : https://files.pythonhosted.org/packages/21/f1/1caf7b7d524aa7021f063509faf987e569f79394f343abadbdf79234667d/yamlloader-1.3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/21/f1/1caf7b7d524aa7021f063509faf987e569f79394f343abadbdf79234667d/yamlloader-1.3.2.tar.gz
Summary  : Ordered YAML loader and dumper for PyYAML.
Group    : Development/Tools
License  : MIT
Requires: pypi-yamlloader-license = %{version}-%{release}
Requires: pypi-yamlloader-python = %{version}-%{release}
Requires: pypi-yamlloader-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
.. image:: https://github.com/Phynix/yamlloader/actions/workflows/ci.yml/badge.svg
:target: https://github.com/Phynix/yamlloader/actions
.. image:: https://img.shields.io/pypi/pyversions/yamlloader.svg
:target: https://pypi.org/project/yamlloader/
.. image:: https://badge.fury.io/py/yamlloader.svg
:target: https://badge.fury.io/py/yamlloader
.. image:: https://coveralls.io/repos/github/Phynix/yamlloader/badge.svg
:target: https://coveralls.io/github/Phynix/yamlloader

%package license
Summary: license components for the pypi-yamlloader package.
Group: Default

%description license
license components for the pypi-yamlloader package.


%package python
Summary: python components for the pypi-yamlloader package.
Group: Default
Requires: pypi-yamlloader-python3 = %{version}-%{release}

%description python
python components for the pypi-yamlloader package.


%package python3
Summary: python3 components for the pypi-yamlloader package.
Group: Default
Requires: python3-core
Provides: pypi(yamlloader)
Requires: pypi(pyyaml)

%description python3
python3 components for the pypi-yamlloader package.


%prep
%setup -q -n yamlloader-1.3.2
cd %{_builddir}/yamlloader-1.3.2
pushd ..
cp -a yamlloader-1.3.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1690989871
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-yamlloader
cp %{_builddir}/yamlloader-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-yamlloader/d614df4a8ba8b9abcbd7464585398394394797c4 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-yamlloader/d614df4a8ba8b9abcbd7464585398394394797c4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
