Summary:	Fast replacement for Ruby's default thread library
Summary(pl):	Szybki zamiennik dla domy¶lnej biblioteki w±tków jêzyka Ruby
Name:		ruby-fastthread
Version:	0.5.2
Release:	1
License:	Ruby
Group:		Development/Libraries
Source0:	http://mongrel.rubyforge.org/releases/gems/fastthread-%{version}.gem
# Source0-md5:	e3e25c2ea1ba92a03f5edeee869e85b9
URL:		http://mongrel.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	ruby-modules
BuildRequires:	setup.rb = 3.3.1
Requires:	ruby-fastthread
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast replacement for Ruby's default thread library.

%description -l pl
Szybki zamiennik dla domy¶lnej biblioteki w±tków jêzyka Ruby.

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
