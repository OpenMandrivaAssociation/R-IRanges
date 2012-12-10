%global packname  IRanges
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.12.6
Release:          1
Summary:          Infrastructure for manipulating intervals on sequences
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-methods R-utils R-stats 
Requires:         R-methods R-utils R-stats 
Requires:         R-RUnit 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-utils R-stats
BuildRequires:    R-methods R-utils R-stats 
BuildRequires:    R-RUnit 

%description
The package provides efficient low-level and highly reusable S4 classes
for storing ranges of integers, RLE vectors (Run-Length Encoding), and,
more generally, data that can be organized sequentially (formally defined
as Vector objects), as well as views on these Vector objects. Efficient
list-like classes are also provided for storing big collections of
instances of the basic classes. All classes in the package use consistent
naming and share the same rich and consistent "Vector API" as much as

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

#%check
#%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/unitTests


%changelog
* Fri Feb 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.12.6-1
+ Revision: 775549
- Import R-IRanges
- Import R-IRanges

