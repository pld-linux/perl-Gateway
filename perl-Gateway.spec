%include	/usr/lib/rpm/macros.perl
%define		pdir	News
%define		pnam	Gateway
Summary:	Gateway Perl module
Summary(cs):	Modul Gateway pro Perl
Summary(da):	Perlmodul Gateway
Summary(de):	Gateway Perl Modul
Summary(es):	M�dulo de Perl Gateway
Summary(fr):	Module Perl Gateway
Summary(it):	Modulo di Perl Gateway
Summary(ja):	Gateway Perl �⥸�塼��
Summary(ko):	Gateway �� ����
Summary(nb):	Perlmodul Gateway
Summary(pl):	Modu� Perla Gateway
Summary(pt):	M�dulo de Perl Gateway
Summary(pt_BR):	M�dulo Perl Gateway
Summary(ru):	������ ��� Perl Gateway
Summary(sv):	Gateway Perlmodul
Summary(uk):	������ ��� Perl Gateway
Summary(zh_CN):	Gateway Perl ģ��
Name:		perl-Gateway
Version:	0.42
Release:	9
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	fa623e920b023428f61a2342e27a6431
Patch0:		%{name}-makefile.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-News-Article
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gateway - Tools for gatewaying messages between news and mail.

%description -l pl
Gateway - narz�dzia do tworzenia bramek news<->mail.

%prep
%setup -q -n %{pnam}-%{version}
%patch -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO doc/*
%{perl_vendorlib}/News/Gateway.pm
%{perl_vendorlib}/auto/News
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
