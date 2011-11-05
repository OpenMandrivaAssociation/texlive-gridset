# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/gridset
# catalog-date 2009-11-09 22:36:07 +0100
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-gridset
Version:	0.1
Release:	1
Summary:	Grid, a.k.a. in-register, setting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gridset
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gridset.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gridset.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gridset.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Grid setting -- also known as strict in-register setting -- is
something, that should be done for a lot of documents but is
not easy using LaTeX. The package helps to get the information
needed for grid setting. It does not implement auto grid
setting, but there is a command \vskipnextgrid, that moves to
the next grid position. This may be enough under some
circumstances, but in other circumstances it may fail. Thus
gridset is only one more step for grid setting, not a complete
solution.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gridset/gridset.sty
%doc %{_texmfdistdir}/doc/latex/gridset/gridset.pdf
#- source
%doc %{_texmfdistdir}/source/latex/gridset/README
%doc %{_texmfdistdir}/source/latex/gridset/gridset.dtx
%doc %{_texmfdistdir}/source/latex/gridset/gridset.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
