<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib prefix="tiles" uri="http://tiles.apache.org/tags-tiles" %>

<c:set var="section"><tiles:getAsString name="section"/></c:set>

<div class="navbar navbar-fixed-top">
    <div class="navbar-inner">
        <div class="container">
            <a class="brand" href="#">
                Nifty Topic Hour Challenge
            </a>
            <ul class="nav">

                <c:set var="currentClass"></c:set>
                <c:if test="${section == 'challenge'}">
                    <c:set var="currentClass">class="active"</c:set>
                </c:if>
                <li ${currentClass}><a href="/challenge">Join the Code Challenge</a></li>

                <c:set var="currentClass"></c:set>
                <c:if test="${section == 'rules'}">
                    <c:set var="currentClass">class="active"</c:set>
                </c:if>
                <li ${currentClass}><a href="/rules">House rules</a></li>

                <c:set var="currentClass"></c:set>
                <c:if test="${section == 'gettingstarted'}">
                    <c:set var="currentClass">class="active"</c:set>
                </c:if>
                <li ${currentClass}><a href="/gettingstarted">Clients</a></li>


                <c:set var="currentClass"></c:set>
                <c:if test="${section == 'serverstatus'}">
                    <c:set var="currentClass">class="active"</c:set>
                </c:if>
                <li ${currentClass}><a href="/serverstatus">Server Status</a></li>

                <c:set var="currentClass"></c:set>
                <c:if test="${section == 'showgame'}">
                    <c:set var="currentClass">class="active"</c:set>
                </c:if>
                <li ${currentClass}><a href="/showgame">Show games</a></li>

            </ul>
        </div>
    </div>
</div>
