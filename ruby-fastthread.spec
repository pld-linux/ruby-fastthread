Summary:	Fast replacement for Ruby's default thread library
Summary(pl.UTF-8):   Szybki zamiennik dla domyślnej biblioteki wątków języka Ruby
Name:		ruby-fastthread
Version:	0.6.3
Release:	1
License:	Ruby
Group:		Development/Libraries
Source0:	http://moonbase.rydia.net/software/optimized-locking/fastthread-%{version}.gem
# Source0-md5:	0bb486071df7ab366e6693410ba6a1fc
URL:		http://moonbase.rydia.net/software/optimized-locking/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	ruby-modules
BuildRequires:	setup.rb = 3.3.1
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast replacement for Ruby's default thread library.

%description -l pl.UTF-8
Szybki zamiennik dla domyślnej biblioteki wątków języka Ruby.

%prep
%setup -q -c -T
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .

%build
cd ext/fastthread
ls *.c > MANIFEST
cd ../..
ruby setup.rb config --rbdir=%{ruby_rubylibdir} --sodir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_archdir}/*.so
