#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Component-Client-FTP
Summary:	POE::Component::Client::FTP - Implements an FTP client POE Component
Summary(pl.UTF-8):	POE::Component::Client::FTP - implementacja klienta FTP jako komponentu POE
Name:		perl-POE-Component-Client-FTP
Version:	0.22
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/POE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7729fd9c950cc722d7a43b1f3ef93540
URL:		http://search.cpan.org/dist/POE-Component-Client-FTP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE >= 0.38
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE Client module for FTP.

%description -l pl.UTF-8
Moduł klienta POE dla FTP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
PERL_MM_USE_DEFAULT=1 \
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Component/Client/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
