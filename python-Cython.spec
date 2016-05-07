#
# Conditional build:
%bcond_without	python2		# CPython 2.x module
%bcond_without	python3		# CPython 3.x module

%define		module	Cython

Summary:	Language for writing Python Extension Modules (Python 2.x version)
Summary(pl.UTF-8):	Język służący do pisania modułów rozszerzających Pythona (wersja dla Pythona 2.x)
Name:		python-%{module}
Version:	0.23.4
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
Source0:	http://cython.org/release/%{module}-%{version}.tar.gz
# Source0-md5:	157df1f69bcec6b56fd97e0f2e057f6e
URL:		http://cython.org/
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python >= 1:2.6
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-2to3 >= 1:3.2
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
Requires:	python-devel >= 1:2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautocompressdoc	*.c

%description
Cython lets you write code that mixes Python and C data types any way
you want, and compiles it into a C extension for Python. Cython is
based on Pyrex.

This package contains Cython module for Python 2.x.

%description -l pl.UTF-8
Cython pozwala pisać kod zawierający dane Pythona i języka C połączone
w jakikolwiek sposób i kompiluje to jako rozszerzenie C dla Pythona.
Cython jest oparty na Pyreksie.

Ten pakiet zawiera moduł Cython dla Pythona 2.x.

%package -n python3-Cython
Summary:	Language for writing Python Extension Modules (Python 3.x version)
Summary(pl.UTF-8):	Język służący do pisania modułów rozszerzających Pythona (wersja dla Pythona 3.x)
Group:		Libraries/Python
Requires:	python3-devel >= 1:3.2

%description -n python3-Cython
Cython lets you write code that mixes Python and C data types any way
you want, and compiles it into a C extension for Python. Cython is
based on Pyrex.

This package contains Cython module for Python 3.x.

%description -n python3-Cython -l pl.UTF-8
Pyrex pozwala pisać kod zawierający dane Pythona i języka C połączone
w jakikolwiek sposób i kompiluje to jako rozszerzenie C dla Pythona.
Cython jest oparty na Pyreksie.

Ten pakiet zawiera moduł Cython dla Pythona 3.x.

%package examples
Summary:	Examples for Cython language
Summary(pl.UTF-8):	Przykłady programów w języku Cython
Group:		Libraries/Python
Obsoletes:	python3-Cython-examples

%description examples
This package contains example programs for Cython language.

%description examples -l pl.UTF-8
Pakiet zawierający przykładowe programy napisane w języku Cython.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/cython{,3}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/cythonize{,3}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/cygdb{,3}
%endif

%if %{with python2}
%py_install

find $RPM_BUILD_ROOT%{py_sitedir} -name "*.py" -a ! -name 'Lexicon.py' -exec rm -f {} \;
%endif

cp -a Demos/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc COPYING.txt README.txt ToDo.txt USAGE.txt Doc/*.html Doc/*.c
%attr(755,root,root) %{_bindir}/cython
%attr(755,root,root) %{_bindir}/cythonize
%attr(755,root,root) %{_bindir}/cygdb
%{py_sitedir}/cython.py[co]
%{py_sitedir}/Cython
%{py_sitedir}/pyximport
%{py_sitedir}/Cython-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-Cython
%defattr(644,root,root,755)
%doc COPYING.txt README.txt ToDo.txt USAGE.txt Doc/*.html Doc/*.c
%attr(755,root,root) %{_bindir}/cython3
%attr(755,root,root) %{_bindir}/cythonize3
%attr(755,root,root) %{_bindir}/cygdb3
%{py3_sitedir}/cython.py
%{py3_sitedir}/__pycache__/cython.*
%{py3_sitedir}/Cython
%{py3_sitedir}/pyximport
%{py3_sitedir}/Cython-%{version}-py*.egg-info
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
