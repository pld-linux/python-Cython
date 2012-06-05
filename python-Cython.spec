
%define		module	Cython

Summary:	Language for writing Python Extension Modules
Summary(pl.UTF-8):	Język służący do pisania modułów rozszerzających Pythona
Name:		python-%{module}
Version:	0.16
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	http://www.cython.org/release/%{module}-%{version}.tar.gz
# Source0-md5:	7934186ada3552110aba92062fa88b1c
URL:		http://www.cython.org/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel
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
Cython pozwala pisać kod zawierający dane Pythona i języka C połączone
w jakikolwiek sposób i kompiluje to jako rozszerzenie C dla Pythona.
Cython jest oparty na Pyreksie.

%package examples
Summary:	Examples for Cython language
Summary(pl.UTF-8):	Przykłady programów w języku Cython
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Cython language.

%description examples -l pl.UTF-8
Pakiet zawierający przykładowe programy napisane w języku Cython.

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
%doc COPYING.txt README.txt ToDo.txt USAGE.txt Doc/*.html Doc/*.c
%attr(755,root,root) %{_bindir}/cython
%attr(755,root,root) %{_bindir}/cygdb
%{py_sitedir}/cython.py[co]
%{py_sitedir}/Cython
%{py_sitedir}/pyximport
%{py_sitedir}/Cython-*.egg-info

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
