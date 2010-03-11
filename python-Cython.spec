
%define		module	Cython

Summary:	Language for writing Python Extension Modules
Summary(pl.UTF-8):	Język służący do pisania modułów rozszerzających Pythona
Name:		python-%{module}
Version:	0.12.1
Release:	1
License:	PSF
Group:		Libraries/Python
Source0:	http://www.cython.org/release/%{module}-%{version}.tar.gz
# Source0-md5:	cf9f98e982258f8516620277975016f3
URL:		http://www.cython.org/
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
%pyrequires_eq	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautocompressdoc	*.c

%description
Cython lets you write code that mixes Python and C data types any way
you want, and compiles it into a C extension for Python. Cython is
based on Pyrex.

%description -l pl.UTF-8
Pyrex pozwala pisać kod zawierający dane Pythona i języka C połączone
w jakikolwiek sposób i kompiluje to jako rozszerzenie C dla Pythona.
Cython jest oparty na Pyreksie.

%package examples
Summary:	Examples for Pyrex language
Summary(pl.UTF-8):	Przykłady programów w języku Pyrex
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Pyrex language.

%description examples -l pl.UTF-8
Pakiet zawierający przykładowe programy napisane w języku Pyrex.

%prep
%setup -q -n %{module}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-purelib=%{py_sitescriptdir} \
	-O2

find $RPM_BUILD_ROOT%{py_sitedir} -name "*.py" -a ! -name 'Lexicon.py' -exec rm -f {} \;

cp -a Demos/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt ToDo.txt USAGE.txt Doc/*.html Doc/*.c
%attr(755,root,root) %{_bindir}/cython
%{py_sitedir}/cython.py[co]
%{py_sitedir}/Cython
%{py_sitedir}/pyximport
%{py_sitedir}/Cython-*.egg-info

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
