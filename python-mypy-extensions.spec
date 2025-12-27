Name:		python-mypy-extensions
Version:	1.1.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/m/mypy_extensions/mypy_extensions-%{version}.tar.gz
Summary:	Type system extensions for programs checked with the mypy type checker.
URL:		https://pypi.org/project/mypy-extensions/
License:	None
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python
BuildArch:	noarch

%rename python-mypy_extensions

%description
Type system extensions for programs checked with the mypy type checker.

%files
%{py_sitedir}/__pycache__/*
%{py_sitedir}/mypy_extensions.py
%{py_sitedir}/mypy_extensions-*.*-info
