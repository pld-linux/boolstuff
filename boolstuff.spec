Summary:	BoolStuff is a C++ library that supports a few operations on boolean expression binary trees
Name:		boolstuff
Version:	0.1.13
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://perso.b2b2c.ca/sarrazip/dev/%{name}-%{version}.tar.gz
# Source0-md5:	084a834f8b4c59f690f1dcf2f385d404
URL:		http://perso.b2b2c.ca/sarrazip/dev/boolstuff.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BoolStuff is a C++ library that supports a few operations on boolean
expression binary trees. The main features are:

a simple boolean expression parser (supports operators AND, OR and
NOT, as well as parentheses); an algorithm to convert a boolean
expression binary tree into its Disjunctive Normal Form (this
algorithm supports the NOT operator); a function that determines if an
expression tree is in DNF.

%package devel
Summary:	Header files for boolstuff library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for boolstuff library.

%package tools
Summary:	Commandline boolstuff tools
Group:		Applications

%description tools
Commandline boolstuff tools.

%prep
%setup -q
echo "AC_CONFIG_MACRO_DIR([macros])" >> configure.ac

%build
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}
install examples/{*.cpp,*.pl} $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%{_libdir}/lib*.la
%{_mandir}/man3/boolstuff.3*
%{_examplesdir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_includedir}/boolstuff-0.1
%{_pkgconfigdir}/*.pc

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/booldnf.1*
