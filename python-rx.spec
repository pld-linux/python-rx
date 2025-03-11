#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Reactive Extensions (Rx) for Python
Summary(pl.UTF-8):	Rozszerzenia Reactive (Rx) dla Pythona
Name:		python-rx
# keep 1.x here for python2 support
Version:	1.6.3
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/Rx/
Source0:	https://files.pythonhosted.org/packages/source/R/Rx/Rx-%{version}.tar.gz
# Source0-md5:	7a389368998d2cd00882af8b483f1037
URL:		https://pypi.org/project/Rx/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-nose
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-nose
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reactive Extensions for Python (RxPY) is a set of libraries for
composing asynchronous and event-based programs using observable
sequences and LINQ-style query operators in Python.

%description -l pl.UTF-8
Reactive Extensions dla Pythona (RxPY) to zbiór bibliotek do tworzenia
w Pythonie programów asynchronicznych i opartych na zdarzeniach przy
użyciu obserwowalnych sekwencji i operatorów zapytań w stylu LINQ.

%package -n python3-rx
Summary:	Reactive Extensions (Rx) for Python
Summary(pl.UTF-8):	Rozszerzenia Reactive (Rx) dla Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-rx
Reactive Extensions for Python (RxPY) is a set of libraries for
composing asynchronous and event-based programs using observable
sequences and LINQ-style query operators in Python.

%description -n python3-rx -l pl.UTF-8
Reactive Extensions dla Pythona (RxPY) to zbiór bibliotek do tworzenia
w Pythonie programów asynchronicznych i opartych na zdarzeniach przy
użyciu obserwowalnych sekwencji i operatorów zapytań w stylu LINQ.

%prep
%setup -q -n Rx-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
nosetests-%{py_ver}
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
nosetests-%{py3_ver}
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/rx
%{py_sitescriptdir}/Rx-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-rx
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/rx
%{py3_sitescriptdir}/Rx-%{version}-py*.egg-info
%endif
