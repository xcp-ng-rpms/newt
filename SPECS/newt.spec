%global package_speccommit a0e36e9d4899d95ebbcc1f39304eaf0f16772c02
%global usver 0.52.23
%global xsver 4
%global xsrel %{xsver}%{?xscount}%{?xshash}

%if 0%{?xenserver} < 9
%global with_python2 1
%endif

Summary: A library for text mode user interfaces
Name: newt
Version: 0.52.23
Release: %{?xsrel}%{?dist}
License: LGPLv2
URL: https://pagure.io/newt
Source0: newt-0.52.23.tar.gz
BuildRequires: make
BuildRequires: gcc popt-devel python3-devel slang-devel
%{?with_python2:BuildRequires: python2-devel}

%package devel
Summary: Newt windowing toolkit development files
Requires: slang-devel %{name} = %{version}-%{release}

%Description
Newt is a programming library for color text mode, widget based user
interfaces.  Newt can be used to add stacked windows, entry widgets,
checkboxes, radio buttons, labels, plain text fields, scrollbars,
etc., to text mode user interfaces.  This package also contains the
shared library needed by programs built with newt, as well as a
/usr/bin/dialog replacement called whiptail.  Newt is based on the
slang library.

%description devel
The newt-devel package contains the header files and libraries
necessary for developing applications which use newt.  Newt is a
development library for text mode user interfaces.  Newt is based on
the slang library.

Install newt-devel if you want to develop applications which will use
newt.

%if 0%{?with_python2}
%package -n python2-newt
%{?python_provide:%python_provide python2-newt}
# Remove before F30
Provides: %{name}-python = %{version}-%{release}
Obsoletes: %{name}-python < 0.52.15-5
Summary: Python 2 bindings for newt
Requires: %{name} = %{version}-%{release}

%description -n python2-newt
The python2-newt package contains the Python 2 bindings for the newt library
providing a python API for creating text mode interfaces.
%endif


%package -n python3-newt
%{?python_provide:%python_provide python3-newt}
# Remove before F30
Provides: %{name}-python3 = %{version}-%{release}
Provides: %{name}-python3 = %{version}-%{release}
Provides: snack = %{version}-%{release}
Summary: Python 3 bindings for newt
Requires: %{name} = %{version}-%{release}

%description -n python3-newt
The python3-newt package contains the Python 3 bindings for the newt library
providing a python API for creating text mode interfaces.

%prep
%setup -q
%autosetup -p1

%build
# gpm support seems to smash the stack w/ we use help in anaconda??
# --with-gpm-support
%configure --without-tcl
%make_build all
chmod 0644 peanuts.py popcorn.py

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/libnewt.a

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS COPYING CHANGES README
%{_bindir}/whiptail
%{_libdir}/libnewt.so.*
%{_mandir}/man1/whiptail.1*

%files devel
%doc tutorial.*
%{_includedir}/newt.h
%{_libdir}/libnewt.so
%{_libdir}/pkgconfig/libnewt.pc

%if 0%{?with_python2}
%files -n python2-newt
%doc peanuts.py popcorn.py
%{python2_sitearch}/*.so
%{python2_sitearch}/*.py*
%endif

%files -n python3-newt
%doc peanuts.py popcorn.py
%{python3_sitearch}/*.so
%{python3_sitearch}/*.py*
%{python3_sitearch}/__pycache__/*.py*

%changelog
* Tue Nov 21 2023 Andrew Cooper <andrew.cooper3@citrix.com> - 0.52.23-4
- Another build. v0.52.23-3 was already used

* Tue Nov 21 2023 Andrew Cooper <andrew.cooper3@citrix.com> - 0.52.23-3
- Fix up the Provide/Obsoletes so package upgrade works

* Mon Sep 25 2023 Gerald Elder-Vass <gerald.elder-vass@citrix.com> - 0.52.23-2
- CP-41302: Build newt with python2 & python3

* Wed Aug 23 2023 Lin Liu <lin.liu@citrix.com> - 0.52.23-1
- First imported release

