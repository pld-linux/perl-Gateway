%include	/usr/lib/rpm/macros.perl
Summary:	Gateway perl module
Summary(pl):	Modu³ perla Gateway
Name:		perl-Gateway
Version:	0.42
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/News/Gateway-%{version}.tar.gz
Patch0:		perl-Gateway-makefile.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-News-Article
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gateway - Tools for gatewaying messages between news and mail.

%description -l pl
Gateway - narzêdzia do tworzenia bramek news<->mail.

%prep
%setup -q -n Gateway-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/News/Gateway
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README TODO doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README,TODO}.gz doc/*

%{perl_sitelib}/News/Gateway.pm
%{perl_sitelib}/auto/News/Gateway
%{perl_sitearch}/auto/News/Gateway

%{_mandir}/man3/*

%{_prefix}/src/examples/%{name}-%{version}
